---
title: Programmation par contraintes
author:
  - Xavier Olive
classoption:
  - dvipsnames
  - usenames
header-includes:
  - \usepackage[ruled,boxed,vlined,titlenotnumbered]{algorithm2e}
  - \setmathfont[Scale=0.95]{Fira Math Light}
aspectratio: 169
theme: utopia
compilation:
  - pandoc slides.md -o slides.pdf -t beamer --pdf-engine xelatex
  - pandoc slides.md -o slides.tex -s -t beamer ; xelatex slides
---

## Objectifs du cours

La \alert{programmation par contraintes} définit un formalisme pour définir des problèmes d'optimisation sous contraintes.

Objectifs du cours:

- comprendre et manipuler le formalisme (cours/BE)
- comprendre les principales méthodes de résolution (cours)
- modéliser un problème complexe à l'aide de ce formalisme (projet noté)

## Paradigmes d'optimisation sous contraintes

- Programmation linéaire (simplexe, points intérieurs)
- Programmation linéaire en nombres entiers (recherche arborescente)

- Programmation non linéaire (méthodes de gradient, estimation de densité)

La programmation par contraintes permet de manipuler des  
\alert{contraintes non linéaires sur des variables discrètes}.

Les méthodes de résolution combinent  
\alert{recherche arborescente} et \alert{propagation de contraintes}.

## Glossaire

|     | Abréviations                      |
| --- | --------------------------------- |
| PPC | Programmation par contraintes     |
| CP  | _Constraint Programming_          |
| CSP | _Constraint Satisfaction Problem_ |
| COP | _Constraint Optimisation Problem_ |

# Définitions

## La programmation par contraintes

Un problème CSP $(V, D, C)$ est composé de:

- $V = \left( v_1, v_2, \dots v_n \right)$, les \alert{variables},
- $D = \left( d_1, d_2, \dots d_n \right)$, les \alert{domaines} finis pour chacune des variables de $V$;
- $C = \left( c_1, c_2, \dots c_m \right)$, une séquence de \alert{contraintes}, chacune définie par un couple $\left( s_i, r_i \right)$:
  - $s_i$ est une séquence de variables;
  - $r_i$ est une \alert{relation} définie par un sous-ensemble du produit cartésien $d_{i_1} \times \dots d_{i_{n_{i}}}$ de valeurs autorisées.

## Définitions

\vfill
\begin{block}{Définition: scope et arité}
Soit $c = (s, r)$, $s$ est aussi appelé \alert{scope} de la contrainte.
La taille du scope est appelée \alert{arité} de la contrainte.
\end{block}
\vfill

\begin{block}{Définition: intension/extension}
On peut définir les contraintes en \alert{extension}:
\begin{equation*}
C: \left( \left( x, y \right), \left\{ \left( 0, 1 \right),
\left( 0, 2 \right), \left( 1, 0 \right), \left( 1, 2 \right),
\left( 2, 0 \right), \left( 2, 1 \right)\right\} \right)
\end{equation*}

    ou en \alert{intension}:
    \begin{equation*}
        C: x \neq y \textrm{ avec } x, y \in \left\{ 0, 1, 2 \right\}
    \end{equation*}

\end{block}
\vfill

## Définitions

\vfill
\begin{block}{Définition: instanciation}
Étant donné un CSP $(V, D, C)$, on appelle \alert{instanciation}
$\mathcal{A}$ de $Y = \left\{ v_{y_1}, \dots v_{y_m} \right\} \subset
    V$, une application qui associe à chaque variable $v_{y_i}$ une valeur
$\mathcal{A}\left( v_{y_i} \right) \in d_{y_i}$.
\end{block}
\vfill
\begin{block}{Définition: satisfaction de contrainte}
Une instanciation $\mathcal{A}$ de $Y$ \alert{satisfait la contrainte}
$c_i = \left( s_i, r_i \right)$ de $C$:
\begin{equation*}
\mathcal{A} \vDash c_i \Leftrightarrow s_i \subset Y \wedge
\mathcal{A} \left( s_i \right) \in r_i
\end{equation*}
\end{block}
À l'opposé, on parle de \alert{violation de contrainte}.

\vfill

## Instanciation cohérente

Une instanciation $\mathcal{A}$ de $Y \subset X$ est \alert{cohérente} ssi pour toute contrainte $c_i=\left( s_i, r_i \right) \in C \textrm{ telle que } s_i \subset Y, \mathcal{A} \vDash c_i$.

Une instanciation est cohérente si elle ne viole aucune contrainte.

- Une \alert{solution} est une instanciation cohérente de $X$.
- Un \alert{CSP est cohérent} s'il a au moins une solution.

## Instanciation globalement cohérente

Une instanciation $\mathcal{A}$ de $Y \subset X$ est \alert{globalement cohérente} ssi il existe une solution $\mathcal{S}$ telle que $\mathcal{A} \subset \mathcal{S}$.

Si une instanciation n'est pas globalement cohérente, il n'est pas possible de l'étendre en une solution.

## Macro-structure d'un CSP

Représentation sous forme d'un \alert{graphe de contraintes}

\begin{tikzpicture}[scale=1.5]

    \tikzstyle{cstr}=[draw,circle,mLightBrown,bottom color=mLightBrown,
    top color= white, text=violet ,minimum width=.8em];
    \tikzstyle{vname}=[draw,circle,mDarkTeal,bottom color=mDarkTeal,
    top color= white, text=black, minimum width=1.3em];

    \foreach \place/\name in {{(0,-1)/v_3}, {(0,1)/v_2}, {(-1,0)/v_1}}
    \node[vname] (\name) at \place {} node[above of=\name,yshift=-1.5em, xshift=-1em] {$\name$};

    \node[vname] (v_4) at (1,0) {} node[above of=v_4,yshift=-1.5em, xshift=1em] {$v_4$};

    \foreach \place/\name in {{(-.5,.5)/c_1}, {(-.2,0)/c_4}, {(.5,.5)/c_2}, {(.5, -.5)/c_3}}
    \node[cstr] (\name) at \place {} node[below of=\name, yshift=2em, xshift=.8em] {$\name$};

    \draw[] (c_4) -- (v_1) -- (c_1) -- (v_2) -- (c_2) -- (v_4) -- (c_3) -- (v_3) -- (c_4) -- (v_2);

\end{tikzpicture}

- sommets: les variables et les contraintes du CSP
- arité d'une contrainte: degré des sommets _contrainte_
- degré d'une variable: degré des sommets _variable_

## Micro-structure d'un CSP

\begin{tikzpicture}[yscale=1.8, xscale=4]

    \tikzstyle{cstr}=[draw,circle,mLightBrown,bottom color=mLightBrown,
    top color= white, text=violet ,minimum width=.8em];
    \tikzstyle{vname}=[draw,circle,mDarkTeal,bottom color=mDarkTeal,
    top color= white, text=black, minimum width=1.3em];

    \foreach \place/\name/\value in {{(0,-1)/v_3/2}, {(1,0)/v_4/3}, {(0,1)/v_2/2}, {(-1,0)/v_1/2}}
        {
            \node [
                rectangle, fill=white, rounded corners=3pt, draw,
                yshift=-.2em, xshift=1.3ex, anchor=north,
                minimum width=4em, minimum height=2*\value em,
                label=$\name$,
            ] (\name) at \place {};

            \foreach \i in {1,...,\value}
            \node[vname, yshift=-1.5*\i em] (\name\i) at \place {} node[right of=\name\i, xshift=-1em] {\i};
        }

    \foreach \place/\name/\label/\value/\anchor in {{(-.5,.5)/c_1/$v_1=v_2$/2/south east}, {(-.5,-.8)/c_4/$v_1 + v_2 + v_3 \leq 3$/1/north east}, {(.5,.5)/c_2/$v_2 < v_4$/3/south west}, {(.5, -.5)/c_3/$v_3 \neq v_4$/3/south east}}
        {
            \node[anchor=\anchor, yshift=-1em] (\name) at \place {$\name:$ \label} ;
            \foreach \i in {1,...,\value}
            \node[cstr, yshift=-\i em)] (\name\i) at \place {};
        }

    \draw (v_11) -- (c_11) -- (v_21) -- (c_41);
    \draw (v_12) -- (c_12) -- (v_22) -- (c_23) -- (v_43);
    \draw (v_11) -- (c_41) -- (v_31) -- (c_31) -- (v_42) -- (c_21) -- (v_21) -- (c_22) -- (v_43) -- (c_32) -- (v_31);
    \draw (v_32) -- (c_31) -- (v_41);
    \draw (v_43) -- (c_33) -- (v_32);

\end{tikzpicture}

- Représentation explicite des domaines et combinaisons de valeurs autorisées

# Exemples

## Coloriage de graphe

Comment colorer la carte de sorte que deux régions voisines soient de couleurs différentes, en utilisant au plus $k$ couleurs?

\begin{center}
\begin{minipage} {.4\textwidth}
\includegraphics[width=\textwidth]{images/france_map.pdf}
\end{minipage}
\hspace{1cm}
\begin{minipage} {.4\textwidth}
\begin{tikzpicture}[yscale=.45, xscale=.3]
\tikzstyle{every node}=[shape=circle, shading=ball, scale=0.7];
% Bayonne
\node [ball color=OliveGreen!50] (aq) at (-1.48, 43.48) {};
% Toulouse
\node [ball color=YellowOrange!50] (mp) at (1.45, 43.62) {};
% Montpellier
\node [ball color=MidnightBlue!50] (lr) at (3.87, 43.61) {};
% Nice
\node [ball color=YellowOrange!50] (paca) at (7.27, 43.7) {};
\node [ball color=BrickRed!50, below right of=paca] (cor) {};
% La Rochelle
\node [ball color=BrickRed!50] (pc) at (-1.18, 46.17) {};
% Limoges
\node [ball color=MidnightBlue!50] (li) at (1.25, 45.83) {};
% Clermont-Ferrand
\node [ball color=BrickRed!50] (au) at (3.08, 45.78) {};
% Grenoble
\node [ball color=OliveGreen!50] (ra) at (5.72, 45.19) {};
% Nantes
\node [ball color=MidnightBlue!50] (pl) at (-1.57, 47.23) {};
% Orléans
\node [ball color=OliveGreen!50] (ce) at (1.9, 47.9) {};
% Auxerre
\node [ball color=YellowOrange!50] (bo) at (3.56, 47.81) {};
% Besançon
\node [ball color=BrickRed!50] (fc) at (6.02, 47.240) {};
% Brest
\node [ball color=OliveGreen!50] (br) at (-4.5, 48.39) {};
% Caen
\node [ball color=YellowOrange!50] (bn) at (-0.36, 49.19) {};
% Rouen
\node [ball color=BrickRed!50] (hn) at (1.08, 49.44) {};
% Paris
\node [ball color=MidnightBlue!50] (if) at (2.34, 48.86) {};
% Reims
\node [ball color=OliveGreen!50] (ca) at (4.03, 49.25) {};
% Metz
\node [ball color=MidnightBlue!50] (lo) at (6.18, 49.12) {};
% Strasbourg
\node [ball color=OliveGreen!50] (al) at (7.76, 48.58) {};
% Amiens
\node [ball color=YellowOrange!50] (pi) at (2.3, 49.9) {};
% Lille
\node [ball color=BrickRed!50] (np) at (3.07, 50.64) {};

            \path[gray!70, draw] (aq) -- (mp) -- (lr) -- (paca) -- (cor);
            \path[gray!70, draw] (aq) -- (li) -- (mp) -- (au) -- (ra) -- (paca);
            \path[gray!70, draw] (aq) -- (pc) -- (li) -- (ce) -- (pl) -- (pc);
            \path[gray!70, draw] (pl) -- (br) -- (bn) -- (hn) -- (ce) -- (if) -- (pi);
            \path[gray!70, draw] (pc) -- (ce) -- (bn) -- (pl);
            \path[gray!70, draw] (ra) -- (lr) -- (au) -- (ce) -- (bo) -- (au) -- (li);
            \path[gray!70, draw] (bo) -- (fc) -- (al) -- (lo) -- (fc) -- (ca) -- (pi);
            \path[gray!70, draw] (lo) -- (ca) -- (bo) -- (ra) -- (fc) ;
            \path[gray!70, draw] (pi) -- (np) -- (ca) -- (if) -- (bo);
            \path[gray!70, draw] (if) -- (hn) -- (pi);
        \end{tikzpicture}
    \end{minipage}

\end{center}

## Le problème des $n$ reines

\begin{columns}[c]
\begin{column}{30mm}
\centering
\begin{tikzpicture}[scale=0.5]
\foreach \i in {0,...,3}
\foreach \j in {0,...,3}
{
\fill[Gray!60] (2*\j,2*\i) rectangle (2*\j+1,2*\i+1);
\fill[Gray!60] (2*\j+1,2*\i+1) rectangle (2*\j+2,2*\i+2);
}

            \draw[thin,black] (0,0) rectangle (8,8);
            \begin{scope}[xshift=0.5cm,yshift=5.45cm, scale=0.4]
                \input{tikz_queen}
            \end{scope}
            \begin{scope}[xshift=1.5cm,yshift=3.45cm, scale=0.4]
                \input{tikz_queen}
            \end{scope}
            \begin{scope}[xshift=2.5cm,yshift=6.45cm, scale=0.4]
                \input{tikz_queen}
            \end{scope}
            \begin{scope}[xshift=3.5cm,yshift=0.45cm, scale=0.4]
                \input{tikz_queen}
            \end{scope}
            \begin{scope}[xshift=4.5cm,yshift=7.45cm, scale=0.4]
                \input{tikz_queen}
            \end{scope}
            \begin{scope}[xshift=5.5cm,yshift=1.45cm, scale=0.4]
                \input{tikz_queen}
            \end{scope}
            \begin{scope}[xshift=6.5cm,yshift=4.45cm, scale=0.4]
                \input{tikz_queen}
            \end{scope}
            \begin{scope}[xshift=7.5cm,yshift=2.45cm, scale=0.4]
                \input{tikz_queen}
            \end{scope}

        \end{tikzpicture}
    \end{column}

    \begin{column}{65mm}
        Comment placer $n$ reines sur un échiquier $n\times n$ de sorte
        qu'aucune reine n'en attaque une autre?
    \end{column}

\end{columns}

## Le sudoku

\begin{columns}[c]
\begin{column}{30mm}
\centering
\begin{tikzpicture}[scale=0.5]
\fill[black!20] (3,3) rectangle (6,6);
\fill[black!20] (0,5) rectangle (9,6);
\fill[black!20] (3,0) rectangle (4,9);
\draw[thick,black] (0,0) rectangle (9,9);
\foreach \i in {1,2,4,5,7,8}
{\draw[very thin,black] (\i,0) -- (\i,9);
\draw[very thin,black] (0,\i) -- (9,\i);}
\foreach \i in {3,6}
{\draw[thick,black] (\i,0) -- (\i,9);
\draw[thick,black] (0,\i) -- (9,\i);}

    \path (.5, 8.5) node {$\sf 7$}; \path (1.5, 8.5) node {$\sf 5$};
    \path (2.5, 8.5) node {$\sf 8$}; \path (4.5, 8.5) node {$\sf 3$};

    \path (1.5, 7.5) node {$\sf 4$}; \path (4.5, 7.5) node {$\sf 8$};
    \path (6.5, 7.5) node {$\sf 3$}; \path (7.5, 7.5) node {$\sf 7$};

    \path (2.5, 6.5) node {$\sf 3$}; \path (5.5, 6.5) node {$\sf 2$};
    \path (7.5, 6.5) node {$\sf 8$};

    \path (5.5, 5.5) node {$\sf 4$}; \path (6.5, 5.5) node {$\sf 1$};
    \path (8.5, 5.5) node {$\sf 3$};

    \path (.5, 4.5) node {$\sf 4$}; \path (3.5, 4.5) node {$\sf 3$};
    \path (5.5, 4.5) node {$\sf 5$}; \path (8.5, 4.5) node {$\sf 8$};

    \path (.5, 3.5) node {$\sf 3$}; \path (2.5, 3.5) node {$\sf 7$};
    \path (3.5, 3.5) node {$\sf 8$};

    \path (1.5, 2.5) node {$\sf 6$}; \path (3.5, 2.5) node {$\sf 1$};

    \path (1.5, 1.5) node {$\sf 3$}; \path (2.5, 1.5) node {$\sf 5$};
    \path (4.5, 1.5) node {$\sf 9$}; \path (7.5, 1.5) node {$\sf 4$};

    \path (4.5, .5) node {$\sf 5$}; \path (6.5, .5) node {$\sf 8$};
    \path (7.5, .5) node {$\sf 9$}; \path (8.5, .5) node {$\sf 1$};

\end{tikzpicture}
\end{column}

\begin{column}{65mm}
Placer des chiffres qui doivent être tous différents sur chaque ligne, chaque colonne et chaque sous-carré.
\end{column}
\end{columns}

## Problème de séquençage de tâches

Comment planifier des tâches ayant chacune:

- une durée d'exécution,
- une date de démarrage au plus tard,
- des ressources à mobiliser,
- des contraintes d'antériorité

On parle en anglais du problème de _jobshop_.

## Autres problèmes classiques

- **Problème de configuration de produit** (_Product configuration problem_)

  Sélectionner des composants dans un catalogue pour assembler un produit conforme aux attentes du client tout en respectant les contraintes techniques.

  p. ex. configuration de matériel informatique

- **Problème de tournée de véhicules** (_Vehicle routing problem_)

  Comment planifier une tournée de véhicule qui minimise le coût de livraison en respectant des contraintes de capacité des véhicules, de fenêtres de temps de livraison, etc.

# Résolution d'un CSP

## Difficulté de la résolution des problèmes

- Même avec peu de variables et de contraintes, l'espace de recherche est tel qu'il conduit à phénomène d'\alert{explosion combinatoire}  
  (complexité $O(m\cdot d^n)$ avec $n$ variables, $d$ la taille max des domaines et $m$ contraintes.)

- Problème \alert{NP-complet}: pas d'algorithme complet connu pour le problème CSP dont la complexité serait polynomiale.

## Exemples

\begin{columns}[c]
\begin{column}{30mm}
\centering
\begin{tikzpicture}[scale=0.5]
\foreach \i in {0,...,3}
\foreach \j in {0,...,3}
{
\fill[Gray] (2*\j,2*\i) rectangle (2*\j+1,2*\i+1);
\fill[Gray] (2*\j+1,2*\i+1) rectangle (2*\j+2,2*\i+2);
}

            \draw[thin,black] (0,0) rectangle (8,8);
            \begin{scope}[xshift=0.5cm,yshift=5.45cm, scale=0.4]
                \input{tikz_queen}
            \end{scope}
            \begin{scope}[xshift=1.5cm,yshift=3.45cm, scale=0.4]
                \input{tikz_queen}
            \end{scope}
            \draw[<->, ultra thick, BrickRed] (2.5, 0.5) -- (2.5, 7.5);
            \begin{scope}[xshift=2.5cm,yshift=4.45cm, scale=0.4]
                \input{tikz_queen}
            \end{scope}

        \end{tikzpicture}
    \end{column}
    \begin{column}{30mm}
        \centering

\begin{tikzpicture}[scale=0.5]
\fill[black!20] (3,3) rectangle (6,6);
\fill[black!20] (0,5) rectangle (9,6);
\fill[black!20] (3,0) rectangle (4,9);
\draw[thick,black] (0,0) rectangle (9,9);
\foreach \i in {1,2,4,5,7,8}
{\draw[very thin,black] (\i,0) -- (\i,9);
\draw[very thin,black] (0,\i) -- (9,\i);}
\foreach \i in {3,6}
{\draw[thick,black] (\i,0) -- (\i,9);
\draw[thick,black] (0,\i) -- (9,\i);}

    \draw[very thick,BrickRed] (0,5) rectangle (9,6);
    \draw[very thick,OliveGreen] (3,0) rectangle (4,9);
    \draw[very thick,MidnightBlue] (3,3) rectangle (6,6);

    \path (3.5,5.5) node[draw, circle, thick, BrickRed, text width=4mm]  {\textcolor{BrickRed}{\tiny$\sf 2,6$\\[-3mm]$\sf 7,9$}};

    \path (.5, 8.5) node {$\sf 7$}; \path (1.5, 8.5) node {$\sf 5$};
    \path (2.5, 8.5) node {$\sf 8$}; \path (4.5, 8.5) node {$\sf 3$};

    \path (1.5, 7.5) node {$\sf 4$}; \path (4.5, 7.5) node {$\sf 8$};
    \path (6.5, 7.5) node {$\sf 3$}; \path (7.5, 7.5) node {$\sf 7$};

    \path (2.5, 6.5) node {$\sf 3$}; \path (5.5, 6.5) node {$\sf 2$};
    \path (7.5, 6.5) node {$\sf 8$};

    \path (5.5, 5.5) node {$\sf 4$}; \path (6.5, 5.5) node {$\sf 1$};
    \path (8.5, 5.5) node {$\sf 3$};

    \path (.5, 4.5) node {$\sf 4$}; \path (3.5, 4.5) node {$\sf 3$};
    \path (5.5, 4.5) node {$\sf 5$}; \path (8.5, 4.5) node {$\sf 8$};

    \path (.5, 3.5) node {$\sf 3$}; \path (2.5, 3.5) node {$\sf 7$};
    \path (3.5, 3.5) node {$\sf 8$};

    \path (1.5, 2.5) node {$\sf 6$}; \path (3.5, 2.5) node {$\sf 1$};

    \path (1.5, 1.5) node {$\sf 3$}; \path (2.5, 1.5) node {$\sf 5$};
    \path (4.5, 1.5) node {$\sf 9$}; \path (7.5, 1.5) node {$\sf 4$};

    \path (4.5, .5) node {$\sf 5$}; \path (6.5, .5) node {$\sf 8$};
    \path (7.5, .5) node {$\sf 9$}; \path (8.5, .5) node {$\sf 1$};

\end{tikzpicture}
\end{column}

\end{columns}

\pause

- Résolution par \alert{recherche arborescente} et \alert{propagation de contraintes}.

## Recherche arborescente

- On parcourt l'espace de recherche des solutions en affectant des valeurs à des variables.  
  Une affectation constitue une _hypothèse_.
- L'ensemble des hypothèses faites à une étape donnée constitue une instanciation partielle, dont on vérifie la cohérence.
- On \alert{parcourt en profondeur un arbre de recherche (DFS)}:
  - un nœud $n$ correspond à l'affectation d'une variable $x$;
  - une arête issue de $n$ correspond à une valeur $a$ affectée à $x$;
  - les feuilles sont des instanciations complètes.
- Si une contrainte portant sur les variables déjà affectées est violée (\emph{backward checking}), on remonte dans l'arbre.

## Exemple

\usetikzlibrary{arrows}
\tikzset{
treenode/.style = {align=center, inner sep=0pt},
% variable
varnode/.style = {treenode, circle, draw, text width=.5em,
fill=black, minimum height=.5em},
done/.style = {treenode, circle, draw=BrickRed, text width=.2em,
fill=BrickRed, minimum height=.2em},
thin/.style = {treenode, circle, draw, text width=.2em,
fill=black, minimum height=.2em},
% hypothèses
hypl/.style = {left, anchor=east, inner sep=6pt},
hypr/.style = {right, anchor=west, inner sep=6pt},
% edges
bt/.style = {very thin, draw=BrickRed},
}

\begin{tikzpicture}[scale=1]
\node [varnode] (x0) {}
child {
node [varnode] (y0) {}
edge from parent node[hypl] {$0$}
}
child {
node [varnode] (y1) {}
child {
node [varnode] (z0) {}
edge from parent node[hypl] {$0$}
}
child {
node [varnode] (z1) {}
child {
node [] {$(1,1,0)$}
edge from parent node[hypl] {$0$}
}
child {
node [] {$(1,1,1)$}
edge from parent node[hypl] {$1$}
}
child {
node [] {$(1,1,2)$}
edge from parent node[hypl] {$2$}
}
child {
node [] {$(1,1,3)$}
edge from parent node[hypl] {$3$}
}
edge from parent node[hypl] {$1$}
}
child {
node [varnode] (z2) {}
edge from parent node[hypl] {$2$}
}
child {
node [varnode] (z3) {}
edge from parent node[hypl] {$3$}
}
edge from parent node[hypl] {$1$}
}
child {
node [varnode] (y2) {}
edge from parent node[hypl] {$2$}
}
child {
node [varnode] (y3) {}
edge from parent node[hypl] {$3$}
};
\node [left of=x0] (x) {x};
\node [left of=y0] (y) {y};
\node [left of=z0] (z) {z};
\draw[dashed] (x) -- (x0);
\draw[dashed] (y) -- (y0) -- (y1) -- (y2) -- (y3);
\draw[dashed] (z) -- (z0) -- (z1) -- (z2) -- (z3);
\end{tikzpicture}

## Exemple

\usetikzlibrary{arrows}
\tikzset{
treenode/.style = {align=center, inner sep=0pt},
% variable
varnode/.style = {treenode, circle, draw, text width=.5em,
fill=black, minimum height=.5em},
done/.style = {treenode, circle, draw=BrickRed, text width=.2em,
fill=BrickRed, minimum height=.2em},
thin/.style = {treenode, circle, draw, text width=.2em,
fill=black, minimum height=.2em},
% hypothèses
hypl/.style = {left, anchor=east, inner sep=6pt},
hypr/.style = {right, anchor=west, inner sep=6pt},
% edges
bt/.style = {very thin, draw=BrickRed},
}

\begin{tikzpicture}[scale=1]
\node [varnode] (x0) {}
child {
node [] (y0) {$(0,\cdot,\cdot)$}
child {
node [BrickRed] (z0) {$(0,0,\cdot)$} edge from parent }
child {
node [varnode] (z1) {} edge from parent }
child {
node [varnode] (z2) {} edge from parent }
child {
node [varnode] (z3) {} edge from parent }
edge from parent
}
child { node [varnode] (y1) {} edge from parent }
child { node [varnode] (y2) {} edge from parent }
child { node [varnode] (y3) {} edge from parent };
\node [left of=x0] (x) {x};
\node [left of=y0] (y) {y};
\draw[dashed] (x) -- (x0);
\draw[dashed] (y) -- (y0) -- (y1) -- (y2) -- (y3);
\draw[BrickRed, very thick] (z0) edge[->, bend left]
node[anchor=east, inner sep=1em, font=\itshape] {backtrack} (y0);
\end{tikzpicture}

- L'assignation partielle $(0,0,\cdot)$ viole la contrainte $x\neq y$: on
  interrompt le parcours en profondeur. On parle alors de \alert{backtracking}.

## Exemple

\usetikzlibrary{arrows}
\tikzset{
treenode/.style = {align=center, inner sep=0pt},
% variable
varnode/.style = {treenode, circle, draw, text width=.5em,
fill=black, minimum height=.5em},
done/.style = {treenode, circle, draw=BrickRed, text width=.2em,
fill=BrickRed, minimum height=.2em},
thin/.style = {treenode, circle, draw, text width=.2em,
fill=black, minimum height=.2em},
% hypothèses
hypl/.style = {left, anchor=east, inner sep=6pt},
hypr/.style = {right, anchor=west, inner sep=6pt},
% edges
bt/.style = {very thin, draw=BrickRed},
}

\begin{tikzpicture}[scale=1]
\node [varnode] (x0) {}
child {
node [] (y0) {$(0,\cdot,\cdot)$}
child {
node [done] (z0) {}
edge from parent [very thin, draw=BrickRed]
}
child {
node [] (z1) {$(0,1,\cdot)$}
child {
node [BrickRed] (r0) {$(0,1,0)$} edge from parent }
child { node [varnode] (r1) {} edge from parent }
child { node [varnode] (r2) {} edge from parent }
child { node [varnode] (r3) {} edge from parent }
edge from parent
}
child { node [varnode] (z2) {} edge from parent }
child { node [varnode] (z3) {} edge from parent }
edge from parent node[hypl] {}
}
child { node [varnode] (y1) {} edge from parent }
child { node [varnode] (y2) {} edge from parent }
child { node [varnode] (y3) {} edge from parent };
\node [left of=x0] (x) {x};
\node [left of=y0] (y) {y};
\node [left of=z0] (z) {z};
\draw[dashed] (x) -- (x0);
\draw[dashed] (y) -- (y0) -- (y1) -- (y2) -- (y3);
\draw[dashed] (z) -- (z0) -- (z1) -- (z2) -- (z3);
\draw[BrickRed, very thick] (r0) edge[->, bend left]
node[anchor=east, inner sep=1em, font=\itshape] {backtrack} (z1);
\end{tikzpicture}

## Exemple

\usetikzlibrary{arrows}
\tikzset{
treenode/.style = {align=center, inner sep=0pt},
% variable
varnode/.style = {treenode, circle, draw, text width=.5em,
fill=black, minimum height=.5em},
done/.style = {treenode, circle, draw=BrickRed, text width=.2em,
fill=BrickRed, minimum height=.2em},
thin/.style = {treenode, circle, draw, text width=.2em,
fill=black, minimum height=.2em},
% hypothèses
hypl/.style = {left, anchor=east, inner sep=6pt},
hypr/.style = {right, anchor=west, inner sep=6pt},
% edges
bt/.style = {very thin, draw=BrickRed},
}

\begin{tikzpicture}[scale=1]
\node [varnode] (x0) {}
child {
node [] (y0) {$(0,\cdot,\cdot)$}
child {
node [done] (z0) {}
edge from parent [very thin, draw=BrickRed]
}
child {
node [] (z1) {$(0,1,\cdot)$}
child {
node [done] (r0) {}
edge from parent [very thin, draw=BrickRed]
}
child {
node [BrickRed] (r1) {$(0,1,1)$} edge from parent }
child { node [varnode] (r2) {} edge from parent }
child { node [varnode] (r3) {} edge from parent }
edge from parent
}
child { node [varnode] (z2) {} edge from parent }
child { node [varnode] (z3) {} edge from parent }
edge from parent
}
child { node [varnode] (y1) {} edge from parent }
child { node [varnode] (y2) {} edge from parent }
child { node [varnode] (y3) {} edge from parent };
\node [left of=x0] (x) {x};
\node [left of=y0] (y) {y};
\node [left of=z0] (z) {z};
\draw[dashed] (x) -- (x0);
\draw[dashed] (y) -- (y0) -- (y1) -- (y2) -- (y3);
\draw[dashed] (z) -- (z0) -- (z1) -- (z2) -- (z3);
\draw[BrickRed, very thick] (r1) edge[->, bend left]
node[anchor=east, inner sep=1em, font=\itshape] {backtrack} (z1);
\end{tikzpicture}

## Exemple

\usetikzlibrary{arrows}
\tikzset{
treenode/.style = {align=center, inner sep=0pt},
% variable
varnode/.style = {treenode, circle, draw, text width=.5em,
fill=black, minimum height=.5em},
done/.style = {treenode, circle, draw=BrickRed, text width=.2em,
fill=BrickRed, minimum height=.2em},
thin/.style = {treenode, circle, draw, text width=.2em,
fill=black, minimum height=.2em},
% hypothèses
hypl/.style = {left, anchor=east, inner sep=6pt},
hypr/.style = {right, anchor=west, inner sep=6pt},
% edges
bt/.style = {very thin, draw=BrickRed},
}

\begin{tikzpicture}[scale=1]
\node [varnode] (x0) {}
child {
node [] (y0) {$(0,\cdot,\cdot)$}
child {
node [done] (z0) {}
edge from parent [very thin, draw=BrickRed]
}
child {
node [] (z1) {$(0,1,\cdot)$}
child {
node [done] (r0) {}
edge from parent [very thin, draw=BrickRed]
}
child {
node [done] (r1) {}
edge from parent [very thin, draw=BrickRed]
}
child {
node [draw, rectangle, very thick, OliveGreen] (r2) {$(0,1,2)$}
edge from parent
}
child { node [varnode] (r3) {} edge from parent }
edge from parent
}
child { node [varnode] (z2) {} edge from parent }
child { node [varnode] (z3) {} edge from parent }
edge from parent
}
child { node [varnode] (y1) {} edge from parent }
child { node [varnode] (y2) {} edge from parent }
child { node [varnode] (y3) {} edge from parent };
\node [left of=x0] (x) {x};
\node [left of=y0] (y) {y};
\node [left of=z0] (z) {z};
\draw[dashed] (x) -- (x0);
\draw[dashed] (y) -- (y0) -- (y1) -- (y2) -- (y3);
\draw[dashed] (z) -- (z0) -- (z1) -- (z2) -- (z3);
\node [below right of=r2, OliveGreen] {\bf Solution trouvée};
\end{tikzpicture}

## Sur le problème des $n$ reines

\includegraphics[width=.95\textwidth]{images/queen-gt.pdf}

- 3 reines: 27 feuilles; 8 reines: plus de 16 millions de feuilles
- $n$ reines: $n^n$ feuilles

## Sur le problème des $n$ reines (avec backtracking)

\includegraphics[width=.9\textwidth]{images/queen-bc.pdf}

# Propagation de contraintes

## Vers plus d'élagage de l'espace de recherche

Idée poursuivie: effectuer des raisonnements plus poussés à chaque nœud de l'arbre de recherche pour essayer de \alert{détecter plus tôt les incohérences}

En particulier, détection d'incohérence par raisonnement sur des contraintes \alert{avant que toutes les variables} de ces contraintes ne soient instanciées.

- pour $c : x = y$ et avec $d_x = \{0,1\}$, $d_y = \{2,3\}$, incohérence détectable immédiatement
- pour $C = \{ c_1,c_2,c_3 \}$ avec $c_1: x < y$, $c_2: y < z$ et $c_3: z < x$, incohérence détectable également (incohérence due à des interactions entre contraintes)

On parle alors de \alert{propagation de contraintes}

## Cohérence locale

Les techniques de cohérence locale ont pour objectif de faire des déductions pour \alert{simplifier un problème donné}.

On effectue des raisonnements locaux afin de déduire qu'une assignation de valeur à une variable ne participe à aucune solution, et qu'il est donc possible de \alert{supprimer cette valeur du domaine}.

## Arc-cohérence

L'arc-cohérence est la plus simple et la plus utilisée des cohérences locales: elle correspond à la \alert{cohérence locale sur toutes les contraintes binaires}.

Un CSP $(V, D, C)$ est arc-cohérent ssi pour toute variable $x\in V$, et pour toute contrainte {binaire} $c = \left( \left\{ x, y \right\}, R \right) \in C$, on a:
\begin{equation*}
\forall a\in d(x)\; \exists b \in d(y),\; (x,a),(y,b) \in R
\end{equation*}

## Arc-cohérence

Un problème qui n'est pas arc-cohérent ne sera pas cohérent.  
\alert{La réciproque n'est pas vraie.}

\tikzset{
treenode/.style = {align=center, inner sep=0pt},
% variable
varnode/.style = {treenode, circle, draw, text width=.5em,
fill=black, minimum height=.5em},
done/.style = {treenode, circle, draw=BrickRed, text width=.2em,
fill=BrickRed, minimum height=.2em},
thin/.style = {treenode, circle, draw, text width=.2em,
fill=black, minimum height=.2em},
% hypothèses
hypl/.style = {left, anchor=east, inner sep=6pt},
hypr/.style = {right, anchor=west, inner sep=6pt},
% edges
bt/.style = {very thin, draw=BrickRed},
}

\begin{minipage}{.2\textwidth}
\begin{center}
\begin{tikzpicture}
\node [varnode] (x0) {}
child {
node [varnode] (x1) {} node[below] {$x_1$}
edge from parent node[left] {$\neq$}
}
child {
node [varnode] (x2) {} node[below] {$x_2$}
edge from parent node[right] {$\neq$}
} node[left] {$x_0$};
\path (x1) edge node[below] {$\neq$} (x2) ;

        \end{tikzpicture}
    \end{center}

\end{minipage}
\begin{minipage}{.7\textwidth}
\begin{enumerate}
\item $x_0, x_1, x_2 \in \left\{ 0, 1 \right\}$
\item En assignant une valeur à $x_0$, on peut toujours assigner des
valeurs à $x_1, x_2$ sans violer les contraintes qui impliquent
$x_0$.
\end{enumerate}
\end{minipage}

## Algorithme pour établir l'arc-cohérence

Fonction de base:  
révision du domaine $d_x$ d'une variable $x$ en raisonnant sur une contrainte $c_{xy}$

\begin{algorithm}[H]
\DontPrintSemicolon
\SetAlgoCaptionSeparator{\unskip}
{
$\mathit{change} \gets \mathit{false}$\;
\For{$a \in d_x$}{
\If{$\nexists b \in d_y, \, \{(x,a),(y,b)\}$ satisfies $c_{xy}$}{
delete $a$ from $\d_x$\; $\mathit{change} \gets \mathit{true}$\;
}
}
\KwRet{$\mathit{change}$}
}
\caption{\hspace{1cm}\texttt{revise}$(x,y)$}
\end{algorithm}

## AC-3

Idée générale: maintien d'une liste de révisions à effectuer

\begin{algorithm}[H]
\DontPrintSemicolon
\SetAlgoCaptionSeparator{\unskip}
%\Begin
{
$Q \gets \{ ( x,y) \,|\, c_{xy} \in C \}\quad$ \textcolor{Gray}{\small \# liste des couples $(x,y)$ à réviser} \;
\While{$Q \neq \emptyset$}{
$(x,y) \gets$ remove one element from $Q$ \;
$\mathit{change} \gets$ \texttt{revise}$(x,y)$ \;
\If{$\mathit{change}$}{
\lIf{$d_x = \emptyset$}{\KwRet{$\mathit{false}\quad$} \textcolor{Gray}{\small \# preuve d'incohérence}}
$Q \gets Q \cup \{ ( z,x) \,|\, c_{zx} \in C \land z \neq y \}\quad$
\textcolor{Gray}{\small \# révisions requises sur les voisins de $x$}
}
}
\KwRet{$\mathit{true}$}
}
\caption{\hspace{1cm}\texttt{AC3}$(V,C)$}
\end{algorithm}

## Arc-cohérence

On utilise généralement les procédures AC$^{\star}$ lors d'une recherche arborescente, pour s'assurer qu'après toute assignation, le sous-problème induit reste arc-cohérent.

On utilise souvent une version \emph{dégradée} de l'arc-cohérence. À l'étape $x_i$, on peut vérifier l'arc-cohérence pour tout couple:

- $\left( x_k, x_i \right)$ tel que $i < k \leq n$ (\emph{forward-checking})
- $\left( x_j, x_k \right)$ tel que $i \leq j < k \leq n$ (\emph{partial look-ahead})
- $\left( x_j, x_k \right)$ tel que $i \leq j \neq k \leq n$ (\emph{full look-ahead})

## Exemple sur le problème des $n$ reines

\begin{columns}[c]
\begin{column}{30mm}

        \centering
        \begin{tikzpicture}[scale=0.45]
            \foreach \i in {0,...,3}
            \foreach \j in {0,...,3}
            {
                \fill[Gray!50] (2*\j,2*\i) rectangle (2*\j+1,2*\i+1);
                \fill[Gray!50] (2*\j+1,2*\i+1) rectangle (2*\j+2,2*\i+2);
            }

            \begin{scope}[xshift=0.5cm,yshift=7.45cm, scale=0.4, BrickRed]
                \input{tikz_queen}
            \end{scope}
            \foreach \i in {1,...,7}
            {
                \fill[BrickRed!60] (.5+\i, 7.5-\i) circle (1ex);
                \fill[BrickRed!60] (.5, 7.5-\i) circle (1ex);
            }
            \draw[thin, black, fill opacity=0] (0,0) rectangle (8,8);
            \pause
            \begin{scope}[xshift=2.5cm,yshift=6.45cm, scale=0.4, OliveGreen]
                \input{tikz_queen}
            \end{scope}
            \fill[OliveGreen!60] (1.5, 5.5) circle (1ex);
            \foreach \i in {2,...,6}
            {
               \fill[OliveGreen!60] (2.5, 6.5-\i) circle (1ex);
               \fill[OliveGreen!60] (1.5+\i, 7.5-\i) circle (1ex);
            }
            \pause
            \begin{scope}[xshift=4.5cm,yshift=5.45cm, scale=0.4,
                MidnightBlue]
                \input{tikz_queen}
            \end{scope}
            \fill[MidnightBlue!40] (1.5, 2.5) circle (1ex);
            \foreach \i in {3,...,5}
            {
                \fill[MidnightBlue!60] (2.5+\i, 7.5-\i) circle (1ex);
                \fill[MidnightBlue!60] (4.5, 5.5-\i) circle (1ex);
            }
            \pause
            \begin{scope}[xshift=1.5cm,yshift=4.45cm, scale=0.4, Mulberry]
                \input{tikz_queen}
            \end{scope}
            \fill[Mulberry!60] (3.5, 2.5) circle (1ex);
            \fill[Mulberry!60] (5.5, 0.5) circle (1ex);
            \fill[Mulberry!60] (1.5, 0.5) circle (1ex);
            \fill[Mulberry!60] (1.5, 1.5) circle (1ex);
            \fill[Mulberry!60] (1.5, 3.5) circle (1ex);
            \draw[Mulberry, ultra thick] (0,2) rectangle (8,3);
        \end{tikzpicture}
    \end{column}

    \begin{column}{65mm}
        {\it Forward-checking}\\[2mm]
        À partir d'une variable $x_i$ donnée, on vérifie l'arc-cohérence
        pour tous les couples $\left( x_k, x_i \right)$ tels que
        $i < k \leq n$.\\[2mm]
         \uncover<4>{
         \begin{itemize}
             \item <alert@4> Plus de valeur possible pour $x_6$: backtrack
         \end{itemize}
     }
    \end{column}

\end{columns}

## Analyse de l'arc-cohérence

Points forts:

- possibilité de l'assurer à moindre coût, en $O(m \cdot d^{2})$ ($O(m \cdot d^{3})$ pour AC-3);
- possibilité de l'assurer avant la recherche arborescente ou pendant;

Points faibles:

- insuffisante pour garantir l'existence d'une solution (possibilité de ne pas détecter certaines incohérences)
- applicable uniquement aux contraintes binaires

# Contraintes globales

## Contraintes globales

- Les \alert{contraintes globales} sont des contraintes particulières avec des mécanismes de propagation optimisés;

- Ces contraintes apportent une sémantique riche;  
  leur efficacité rendent la PPC compétitive sur des problèmes difficiles;

- Catalogue de contraintes globales: http://sofdem.github.io/gccat/

## Alldifferent

\texttt{alldifferent$(x_1, \ldots , x_k)$} (porte sur $k$ variables)

satisfaite ssi: $\forall i \neq j \in [1..k], \, x_i \neq x_j$

Exemple:

${x_{1}} \in \{b,c,d,e\}$  
${x_{2}} \in \{b,c\}$  
${x_{3}} \in \{a,b,c,d\}$  
${x_{4}} \in \{b,c\}$  
$\mbox{\tt alldifferent}(x_{1}, x_{2}, x_{3}, x_{4})$

Établissement facile de l'arc-cohérence généralisée grâce à des techniques d'analyse de graphes

## Alldifferent

Pour propager la contrainte, on part d'un graphe bipartite:

\begin{tikzpicture}[scale=5]

\tikzstyle{val} = [circle, draw=mDarkTeal, bottom color=mDarkTeal, top color=white];
\node[val, label=above left:$a$] (a) {};
\node[val, right of=a, label=above left:$b$] (b) {};
\node[val, right of=b, label=above left:$c$] (c) {};
\node[val, right of=c, label=above left:$d$] (d) {};
\node[val, right of=d, label=above left:$e$] (e) {};

\tikzstyle{var} = [circle, draw=mLightBrown, bottom color=mLightBrown, top color=white];
\node[var, below of=a, xshift=1.5em, label=below left:$x_1$] (x1) {};
\node[var, right of=x1, label=below left:$x_2$] (x2) {};
\node[var, right of=x2, label=below left:$x_3$] (x3) {};
\node[var, right of=x3, label=below left:$x_4$] (x4) {};

\draw (a) -- (x3) -- (b) -- (x1) -- (c) -- (x2) -- (b) -- (x4) -- (c) -- (x3) -- (d) -- (x1) -- (e);

\end{tikzpicture}

## Alldifferent

L'affectation courante est cohérente ssi il existe un \alert{k-matching} dans le graphe bi-partite associé (pour $k$ variables)

L'algorithme de Hopcroft et Karp, teste l'existence d'un k-matching dans un graphe bipartite en $O(s \cdot \sqrt{k})$, avec $s$ somme des tailles des domaines de valeurs

On peut alors supprimer les valeurs non arc-cohérentes en temps polynomial $O(s)$; on peut notamment supprimer rapidement les choix $x_1 = b$, $x_1 = c$, $x_3 = b$, $x_3 = c$)}

## Alldifferent

\begin{columns}[c]
\begin{column}{30mm}
\centering
\begin{tikzpicture}[scale=0.5]

    \draw[thick,black] (0,0) rectangle (9,9);
    \foreach \i in {1,2,4,5,7,8}
    {\draw[very thin,black] (\i,0) -- (\i,9);
    \draw[very thin,black] (0,\i) -- (9,\i);}
    \foreach \i in {3,6}
    {\draw[thick,black] (\i,0) -- (\i,9);
    \draw[thick,black] (0,\i) -- (9,\i);}


    \path (7.5,8.5) node[draw, circle, thick, BrickRed, text width=4mm]  {\textcolor{BrickRed}{\tiny$\sf 1, 2$\\[-3mm]$\sf 6$}};

    \path (.5, 8.5) node {$\sf 7$}; \path (1.5, 8.5) node {$\sf 5$};
    \path (2.5, 8.5) node {$\sf 8$}; \path (4.5, 8.5) node {$\sf 3$};

    \path (1.5, 7.5) node {$\sf 4$}; \path (4.5, 7.5) node {$\sf 8$};
    \path (6.5, 7.5) node {$\sf 3$}; \path (7.5, 7.5) node {$\sf 7$};

    \path (2.5, 6.5) node {$\sf 3$}; \path (5.5, 6.5) node {$\sf 2$};
    \path (7.5, 6.5) node {$\sf 8$};

    \path (5.5, 5.5) node {$\sf 4$}; \path (6.5, 5.5) node {$\sf 1$};
    \path (8.5, 5.5) node {$\sf 3$};

    \path (.5, 4.5) node {$\sf 4$}; \path (3.5, 4.5) node {$\sf 3$};
    \path (5.5, 4.5) node {$\sf 5$}; \path (8.5, 4.5) node {$\sf 8$};

    \path (.5, 3.5) node {$\sf 3$}; \path (2.5, 3.5) node {$\sf 7$};
    \path (3.5, 3.5) node {$\sf 8$};

    \path (1.5, 2.5) node {$\sf 6$}; \path (3.5, 2.5) node {$\sf 1$};

    \path (1.5, 1.5) node {$\sf 3$}; \path (2.5, 1.5) node {$\sf 5$};
    \path (4.5, 1.5) node {$\sf 9$}; \path (7.5, 1.5) node {$\sf 4$};

    \path (4.5, .5) node {$\sf 5$}; \path (6.5, .5) node {$\sf 8$};
    \path (7.5, .5) node {$\sf 9$}; \path (8.5, .5) node {$\sf 1$};

    \path (4.5, -1) node[align=center] {par \alert{arc-cohérence}};

        \end{tikzpicture}

    \end{column}
    \begin{column}{30mm}
        \centering

\begin{tikzpicture}[scale=0.5]
\draw[thick,black] (0,0) rectangle (9,9);
\foreach \i in {1,2,4,5,7,8}
{\draw[very thin,black] (\i,0) -- (\i,9);
\draw[very thin,black] (0,\i) -- (9,\i);}
\foreach \i in {3,6}
{\draw[thick,black] (\i,0) -- (\i,9);
\draw[thick,black] (0,\i) -- (9,\i);}

    \path (7.5,8.5) node[draw, circle, ultra thick, BrickRed]  {\textcolor{BrickRed}{$\bf\sf 1$}};

    \path (.5, 8.5) node {$\sf 7$}; \path (1.5, 8.5) node {$\sf 5$};
    \path (2.5, 8.5) node {$\sf 8$}; \path (4.5, 8.5) node {$\sf 3$};

    \path (1.5, 7.5) node {$\sf 4$}; \path (4.5, 7.5) node {$\sf 8$};
    \path (6.5, 7.5) node {$\sf 3$}; \path (7.5, 7.5) node {$\sf 7$};

    \path (2.5, 6.5) node {$\sf 3$}; \path (5.5, 6.5) node {$\sf 2$};
    \path (7.5, 6.5) node {$\sf 8$};

    \path (5.5, 5.5) node {$\sf 4$}; \path (6.5, 5.5) node {$\sf 1$};
    \path (8.5, 5.5) node {$\sf 3$};

    \path (.5, 4.5) node {$\sf 4$}; \path (3.5, 4.5) node {$\sf 3$};
    \path (5.5, 4.5) node {$\sf 5$}; \path (8.5, 4.5) node {$\sf 8$};

    \path (.5, 3.5) node {$\sf 3$}; \path (2.5, 3.5) node {$\sf 7$};
    \path (3.5, 3.5) node {$\sf 8$};

    \path (1.5, 2.5) node {$\sf 6$}; \path (3.5, 2.5) node {$\sf 1$};

    \path (1.5, 1.5) node {$\sf 3$}; \path (2.5, 1.5) node {$\sf 5$};
    \path (4.5, 1.5) node {$\sf 9$}; \path (7.5, 1.5) node {$\sf 4$};

    \path (4.5, .5) node {$\sf 5$}; \path (6.5, .5) node {$\sf 8$};
    \path (7.5, .5) node {$\sf 9$}; \path (8.5, .5) node {$\sf 1$};

    \path (4.5, -1) node[align=center] {par \alert{k-matching}};

\end{tikzpicture}

    \end{column}

\end{columns}

## Edge-finding

Exemple d'une contrainte $\texttt{noOverlap}(T)$ de \alert{non-chevauchement entre tâches} à réaliser sur une ressource disjonctive (non partageable)

Entrées de la contrainte: un ensemble de tâches $T$ non interruptibles, avec $\forall t \in T$:

- une durée de réalisation $p_t$ (\emph{processing time})
- une date de début au plus tôt $est_t$ (\emph{earliest start time})
- une date de fin au plus tard $let_t$ (\emph{latest end time})

## Edge-finding

Variables de décision manipulées par la contrainte: pour chaque tâche $t \in T$,

- variable \emph{date de début} $\mathit{sta}_t$
- variable \emph{date de fin} $\mathit{end}_t$ ($= \mathit{sta}_t + p_t$)

Domaines de valeurs:  
$d_{\mathit{sta}_t} = [est_t,let_t-p_t]$ et $d_{\mathit{end}_t} = [est_t+p_t,let_t]$

Contrainte $\texttt{noOverlap}(T)$ satisfaite si et seulement si:
$$\forall t, t' \in T, \, t \neq t', \,\, (sta(t) \geq end(t')) \lor (sta(t') \geq end(t))$$

(contrainte portant sur $k = 2 n$ variables avec $n$ le nombre de tâches)

## Edge-finding

Principe: recherche de contraintes de précédence induites entre tâches pour filtrer les domaines de valeurs des variables $sta_t$ / $end_t$

Notations: pour $\Omega \subseteq T$,

- $est_{\Omega} = min_{t \in \Omega} est_t$ (date de début au plus tôt d'une tâche dans $\Omega$)
- $let_{\Omega} = max_{t \in \Omega} let_t$ (date de fin au plus tard d'une tâche dans $\Omega$)
- $p_{\Omega} = \sum_{t \in \Omega} p_t$ (somme des durées des tâches dans $\Omega$)

## Edge-finding

Règle de \alert{propagation des dates au plus tôt}: pour toute tâche $t \in T$ et tout ensemble de tâches $\Omega \subseteq T \setminus \{t\}$,

Si $est_{\Omega \cup \{t\}} + p_{\Omega \cup \{t\}} > let_{\Omega}$, alors $t \gg \Omega$ (tâche $t$ située après les tâches de $\Omega$)

Dans ce cas, \alert{filtrage}: $est_t \gets max(est_t, est_{\Omega} + p_{\Omega} )$

\begin{tikzpicture}[scale=3]

    \node[] (est) at (0, 0) {};
    \node (est_name) at (0, -.3) {$est_{\Omega \cup \{t\}}$};

    \draw[draw=black] (est) rectangle ++(1.7,0.3) node (let) {};
    \draw[draw=mLightBrown, fill=mLightBrown] (let) rectangle ++(.7,-.3);
    \node (let_name) at (1.7, -.3) {$let_{\Omega}$};

    \draw[dashed] (est) -- (est_name);
    \draw[dashed] (let) -- (let_name);

    \node at (.9, .15) {$p_{\Omega \cup \{t\}}$};
    \node[text=mLightBrown,] at (2, .4) {\textbf{\textit{t}}};

\end{tikzpicture}

## Edge-finding

Règle de \alert{propagation des dates au plus tard}: pour toute tâche $t \in T$ et tout ensemble de tâches $\Omega \subseteq T \setminus \{t\}$,

Si $let_{\Omega \cup \{t\}} - p_{\Omega \cup \{t\}} < est_{\Omega}$, alors $t \ll \Omega$ (tâche $t$ située avant les tâches de $\Omega$)

Dans ce cas, \alert{filtrage}: $let_t \gets min(let_t, let_{\Omega} - p_{\Omega})$

\begin{tikzpicture}[scale=3]

    \node[] (est) at (0, 0) {};
    \node (est_name) at (0, -.3) {$est_{\Omega}$};

    \draw[draw=black] (est) rectangle ++(1.7,0.3) node (let) {};
    \draw[draw=mLightBrown, fill=mLightBrown] (est) rectangle ++(-.7,.3);
    \node (let_name) at (1.7, -.3) {$let_{\Omega \cup \{t\}}$};

    \draw[dashed] (est) -- (est_name);
    \draw[dashed] (let) -- (let_name);

    \node at (.9, .15) {$p_{\Omega \cup \{t\}}$};
    \node[text=mLightBrown,] at (-.35, .4) {\textbf{\textit{t}}};

\end{tikzpicture}

## Edge-finding

\def\interval(####1)(####2:####3)(####4:####5)(####6){%
\draw[ultra thick] (####2,####1) -- ++(####3,0);
\draw[ultra thick] (####2,####1-.1) -- ++(0,.2);
\draw[ultra thick] (####2+####3,####1-.1) -- ++(0,.2);
\draw[mLightBrown, fill=mLightBrown] (####4,####1-.25) rectangle ++(####5,.5);
\path (####4,####1-.2) -- node {####6} ++(####5,.4);
}

\begin{tikzpicture}[scale=1]

    \foreach \i in {0,...,8} {
        \node (x\i) at (\i, .2) {\i};
        \draw[dashed] (\i, .5) -- (\i, 3.5);
    }

    \interval(1)(0:6)(2:2)(C);
    \interval(2)(2:3)(2.5:2)(B);
    \interval(3)(0:8)(2.5:2)(A);

\end{tikzpicture}

Pour $t = A$ et $\Omega = \{ B,C \}$:

$est_{A,B,C} (0) +  p_{A,B,C} (7) > let_{B,C} (6)$

Déduction: $A \gg \{B,C\}$, donc $est_{A} \gets max(est_{A}(0), est_{B,C}(0) + p_{B,C}(4) )$

## Edge-finding

\def\interval(####1)(####2:####3)(####4:####5)(####6){%
\draw[ultra thick] (####2,####1) -- ++(####3,0);
\draw[ultra thick] (####2,####1-.1) -- ++(0,.2);
\draw[ultra thick] (####2+####3,####1-.1) -- ++(0,.2);
\draw[mLightBrown, fill=mLightBrown] (####4,####1-.25) rectangle ++(####5,.5);
\path (####4,####1-.2) -- node {####6} ++(####5,.4);
}

\begin{tikzpicture}[scale=1]

    \foreach \i in {0,...,8} {
        \node (x\i) at (\i, .2) {\i};
        \draw[dashed] (\i, .5) -- (\i, 3.5);
    }

    \interval(1)(0:6)(2:2)(C);
    \interval(2)(2:3)(2.5:2)(B);
    \interval(3)(4:4)(4.5:2)(A);

\end{tikzpicture}

Pour $t = A$ et $\Omega = \{ B,C \}$:

$est_{A,B,C} (0) +  p_{A,B,C} (7) > let_{B,C} (6)$

Déduction: $A \gg \{B,C\}$, donc $est_{A} \gets max(est_{A}(0), est_{B,C}(0) + p_{B,C}(4) )$

## Edge-finding

\def\interval(####1)(####2:####3)(####4:####5)(####6){%
\draw[ultra thick] (####2,####1) -- ++(####3,0);
\draw[ultra thick] (####2,####1-.1) -- ++(0,.2);
\draw[ultra thick] (####2+####3,####1-.1) -- ++(0,.2);
\draw[mLightBrown, fill=mLightBrown] (####4,####1-.25) rectangle ++(####5,.5);
\path (####4,####1-.2) -- node {####6} ++(####5,.4);
}

\begin{tikzpicture}[scale=1]

    \foreach \i in {0,...,8} {
        \node (x\i) at (\i, .2) {\i};
        \draw[dashed] (\i, .5) -- (\i, 3.5);
    }

    \interval(1)(0:6)(2:2)(C);
    \interval(2)(2:3)(2.5:2)(B);
    \interval(3)(4:4)(4.5:2)(A);

\end{tikzpicture}

Pour $t = C$ et $\Omega = \{ A,B \}$:

$let_{A,B,C} (8) -  p_{A,B,C} (7) < est_{A,B} (2)$

Déduction: $C \ll \{A,B\}$, donc $let_{C} \gets min(let_{C}(6), eet_{A,B}(8) - p_{A,B}(5) )$

## Edge-finding

\def\interval(####1)(####2:####3)(####4:####5)(####6){%
\draw[ultra thick] (####2,####1) -- ++(####3,0);
\draw[ultra thick] (####2,####1-.1) -- ++(0,.2);
\draw[ultra thick] (####2+####3,####1-.1) -- ++(0,.2);
\draw[mLightBrown, fill=mLightBrown] (####4,####1-.25) rectangle ++(####5,.5);
\path (####4,####1-.2) -- node {####6} ++(####5,.4);
}

\begin{tikzpicture}[scale=1]

    \foreach \i in {0,...,8} {
        \node (x\i) at (\i, .2) {\i};
        \draw[dashed] (\i, .5) -- (\i, 3.5);
    }

    \interval(1)(0:3)(.5:2)(C);
    \interval(2)(2:3)(2.5:2)(B);
    \interval(3)(4:4)(4.5:2)(A);

\end{tikzpicture}

Pour $t = C$ et $\Omega = \{ A,B \}$:

$let_{A,B,C} (8) -  p_{A,B,C} (7) < est_{A,B} (2)$

Déduction: $C \ll \{A,B\}$, donc $let_{C} \gets min(let_{C}(6), eet_{A,B}(8) - p_{A,B}(5) )$

## Edge-finding

In fine, on prouve que $C \ll B \ll A$ par \alert{propagation}

Remarque: des raisonnements disjoints sur les contraintes
$(sta(t) \geq end(t')) \lor (sta(t') \geq end(t))$ pour $t \neq t' \in \{A,B,C\}$ n'auraient rien donné en termes de propagation

D'où l'intérêt d'avoir des techniques de propagation de contraintes spécifiques raisonnant sur des \alert{connaissances globales} présentant une structure particulière

# Bonnes pratiques

## Heuristiques

Taille de l'arbre de recherche exploré fonction de l'ordre choisi pour affecter les variables et de l'ordre dans lequel les valeurs sont choisies

Exemple d'\alert{heuristiques de choix de variable} ($\equiv$ guides):

- choix d'une variable de plus petit domaine courant (\alert{Min-Domain})
- choix d'une variable impliquée dans le plus de contraintes (\alert{Max-Degree})
- choix d'une variable minimisant le ratio taille du domaine par degré (\alert{Min-Domain / Max-Degree})

Principe général: principe \alert{fail-first} (pour détecter des échecs le plus tôt possible)

## Heuristiques

En général, bénéfique d'utiliser des \alert{heuristiques dynamiques}:

Exemples:

- plus petit domaine courant au lieu de plus petit domaine initial
- variables liées avec le plus de contraintes non instanciées étant donné l'affectation courante
- maintien d'un poids associé à chaque contrainte en fonction des échecs rencontrés et choix de variable en fonction de ces poids (\alert{Weighted-Degree})

## Heuristiques

Heuristique de \alert{choix de valeur}: ordre dans lequel les valeurs sont sélectionnées

Principe \alert{first-success}: sélection de la valeur la moins contraignante d'abord, pour trouver des solutions le plus tôt possible

Diversité des \alert{types de branchement}:

- branchement binaire $x = a$ et $x \neq a$
- branchement dichotomique $x \leq a$ et $x > a$
- branchement énumératif $x = 1$, $x = 2$, \ldots $x = m_x$

\alert{Remarque}: très dépendant de l'application (possibilité de définir des heuristiques métier)

## Importance de la modélisation

Souvent \alert{plusieurs modèles candidats} et \alert{choix des variables} très important (détermine l'espace de recherche)

Possibilité d'ajouter des \alert{contraintes en plus} du modèle de base (idem PLNE):

- contraintes redondantes pour accélérer la recherche (contraintes induites qui seraient difficiles à trouver pour les outils et qui se propagent bien)
- contraintes pour casser les symétries (élimination de solutions équivalentes)
- contraintes supprimant des solutions sous-optimales
- contraintes supprimant des solutions optimales mais pas toutes

## Symétries

\begin{center}
\begin{tikzpicture}[scale=0.5]
\begin{scope}

            \fill[OliveGreen!10] (0,0) rectangle (4,4);
            \foreach \i in {0,...,1}
            \foreach \j in {0,...,1}
            {
                \fill[white] (2*\j,2*\i) rectangle (2*\j+1,2*\i+1);
                \fill[white] (2*\j+1,2*\i+1) rectangle (2*\j+2,2*\i+2);
            }
            \draw[thin,black, fill opacity=0] (0,0) rectangle (4,4);

            \begin{scope}[xshift=0.5cm,yshift=3.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}

        \end{scope}

        \begin{scope}[xshift=5cm]
            \fill[OliveGreen!10] (0,0) rectangle (4,4);
            \foreach \i in {0,...,1}
            \foreach \j in {0,...,1}
            { \fill[white] (2*\j,2*\i) rectangle (2*\j+1,2*\i+1);
            \fill[white] (2*\j+1,2*\i+1) rectangle (2*\j+2,2*\i+2); }
            \draw[thin,black, fill opacity=0] (0,0) rectangle (4,4);

            \begin{scope}[xshift=3.5cm,yshift=3.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}

            \begin{scope}[xshift=2cm,yshift=2cm]
                \draw[BrickRed,thick,<-] (-90:.8) to[bend right=45]
                (0:.8) to[bend right=45] (90:.8) to[bend right=45]
                (180:.8);
            \end{scope}
        \end{scope}
        \begin{scope}[xshift=10cm]
            \fill[OliveGreen!10] (0,0) rectangle (4,4);
            \foreach \i in {0,...,1}
            \foreach \j in {0,...,1}
            { \fill[white] (2*\j,2*\i) rectangle (2*\j+1,2*\i+1);
            \fill[white] (2*\j+1,2*\i+1) rectangle (2*\j+2,2*\i+2); }
            \draw[thin,black, fill opacity=0] (0,0) rectangle (4,4);

            \begin{scope}[xshift=3.5cm,yshift=0.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}
            \begin{scope}[xshift=2cm,yshift=2cm,rotate=-90]
                \draw[BrickRed,thick,<-] (-90:.8) to[bend right=45]
                (0:.8) to[bend right=45] (90:.8) to[bend right=45]
                (180:.8);
            \end{scope}

        \end{scope}
        \begin{scope}[xshift=15cm]
            \fill[OliveGreen!10] (0,0) rectangle (4,4);
            \foreach \i in {0,...,1}
            \foreach \j in {0,...,1}
            { \fill[white] (2*\j,2*\i) rectangle (2*\j+1,2*\i+1);
            \fill[white] (2*\j+1,2*\i+1) rectangle (2*\j+2,2*\i+2); }
            \draw[thin,black, fill opacity=0] (0,0) rectangle (4,4);

            \begin{scope}[xshift=0.5cm,yshift=0.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}
            \begin{scope}[xshift=2cm,yshift=2cm,rotate=180]
                \draw[BrickRed,thick,<-] (-90:.8) to[bend right=45]
                (0:.8) to[bend right=45] (90:.8) to[bend right=45]
                (180:.8);
            \end{scope}

        \end{scope}

    \end{tikzpicture}

    \vspace{2mm}

    \begin{tikzpicture}[scale=0.5]
        \begin{scope}

            \fill[OliveGreen!10] (0,0) rectangle (4,4);
            \foreach \i in {0,...,1}
            \foreach \j in {0,...,1}
            { \fill[white] (2*\j,2*\i) rectangle (2*\j+1,2*\i+1);
            \fill[white] (2*\j+1,2*\i+1) rectangle (2*\j+2,2*\i+2); }
            \draw[thin,black, fill opacity=0] (0,0) rectangle (4,4);

            \begin{scope}[xshift=0.5cm,yshift=2.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}
            \begin{scope}[xshift=1.5cm,yshift=0.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}
            \begin{scope}[xshift=2.5cm,yshift=3.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}
            \begin{scope}[xshift=3.5cm,yshift=1.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}

        \end{scope}

        \begin{scope}[xshift=5cm]
            \fill[OliveGreen!10] (0,0) rectangle (4,4);
            \foreach \i in {0,...,1}
            \foreach \j in {0,...,1}
            { \fill[white] (2*\j,2*\i) rectangle (2*\j+1,2*\i+1);
            \fill[white] (2*\j+1,2*\i+1) rectangle (2*\j+2,2*\i+2); }
            \draw[thin,black, fill opacity=0] (0,0) rectangle (4,4);

            \begin{scope}[xshift=0.5cm,yshift=1.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}
            \begin{scope}[xshift=1.5cm,yshift=3.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}
            \begin{scope}[xshift=2.5cm,yshift=0.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}
            \begin{scope}[xshift=3.5cm,yshift=2.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}

                \draw[BrickRed, thick, dashed](2,5) -- (2,-1);
                \draw[BrickRed,thick,<->](1.2,4.5) to[bend left] (2.8,4.5);
        \end{scope}
    \end{tikzpicture}

\end{center}

## Symétries

Une symétrie $\sigma$ sur un CSP est un automorphisme sur l'ensemble des assignations qui laisse l'ensemble des contraintes globalement inchangé.

## Symétries

\begin{minipage}{.3\textwidth}
\centering
\begin{tikzpicture}[scale=.5]
\begin{scope}[xshift=5cm]
\fill[OliveGreen!10] (0,0) rectangle (4,4);
\foreach \i in {0,...,1}
\foreach \j in {0,...,1}
{ \fill[white] (2*\j,2*\i) rectangle (2*\j+1,2*\i+1);
\fill[white] (2*\j+1,2*\i+1) rectangle (2*\j+2,2*\i+2); }
\draw[thin,black, fill opacity=0] (0,0) rectangle (4,4);

            \begin{scope}[xshift=0.5cm,yshift=1.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}
            \begin{scope}[xshift=1.5cm,yshift=3.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}
            \begin{scope}[xshift=2.5cm,yshift=0.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}
            \begin{scope}[xshift=3.5cm,yshift=2.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}

            \draw[BrickRed, thick, dashed](2,5) -- (2,-1);
            \draw[BrickRed,thick,<->](1.2,4.5) to[bend left] (2.8,4.5);
        \end{scope}
    \end{tikzpicture}

\end{minipage}
\begin{minipage}{.6\textwidth}
$\sigma$ est une permutation de variables:
\begin{itemize}
\item $x_1 \rightleftharpoons x_4$
\item $x_2 \rightleftharpoons x_3$
\end{itemize}
\end{minipage}

\begin{minipage}{.3\textwidth}
\centering
\begin{tikzpicture}[scale=.5]
\begin{scope}[xshift=5cm]
\fill[OliveGreen!10] (0,0) rectangle (4,4);
\foreach \i in {0,...,1}
\foreach \j in {0,...,1}
{ \fill[white] (2*\j,2*\i) rectangle (2*\j+1,2*\i+1);
\fill[white] (2*\j+1,2*\i+1) rectangle (2*\j+2,2*\i+2); }
\draw[thin,black, fill opacity=0] (0,0) rectangle (4,4);

            \begin{scope}[xshift=0.5cm,yshift=1.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}
            \begin{scope}[xshift=1.5cm,yshift=3.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}
            \begin{scope}[xshift=2.5cm,yshift=0.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}
            \begin{scope}[xshift=3.5cm,yshift=2.45cm, scale=0.4]
                \input{tikz_queen} \end{scope}

            \draw[BrickRed, thick, dashed](5,2) -- (-1, 2);
            \draw[BrickRed,thick,<->](-.5,1.2) to[bend left] (-.5,2.8);
        \end{scope}
    \end{tikzpicture}

\end{minipage}
\begin{minipage}{.6\textwidth}
$\sigma$ est une permutation de valeurs:
\begin{itemize}
\item $1 \rightleftharpoons 4$
\item $2 \rightleftharpoons 3$
\end{itemize}
\end{minipage}

## Symétries

On peut exploiter les symétries d'un problème pour réduire le domaine de recherche:

- reformulation du problème;
- ajout statique de contraintes;
- ajout dynamique de contraintes;
- \alert{détection de dominance}

Tout l'enjeu consiste à déterminer si détecter les symétries reste moins coûteux que ce que leur exploitation peut rapporter.

# Recherche incomplète

## Recherche incomplète

On accepte de ne pas trouver l'optimum global, mais plutôt de \alert{trouver des bonnes solutions rapidement}, en privilégiant de la recherche dans des voisinages _prometteurs_.

Exploration plus libre et plus diversifiée.

Deux techniques présentées ici:

- min-conflicts;
- large neighbourhood search (LNS)

## min-conflicts

On accepte de relâcher certaines contraintes au début. On travaille sur une amélioration itérative basée sur la minimisation du nombre de \alert{ contraintes non satisfaites}, avec arrêt lorsque ce nombre vaut $0$.

- choix d'une \alert{affectation initiale} $A_0$ quelconque, puis
- choix aléatoire d'une variable $x$ parmi les variables qui interviennent dans au moins une contrainte violée,
- choix d'une valeur $a$ dans le domaine de $x$ de manière à \alert{minimiser le nombre de contraintes non satisfaites} après réaffectation de la variable $x$,
- nouvelle affectation $A_{i+1}$ obtenue à partir de $A_i$ en donnant la valeur $a$ à $x$.

Pour \alert{diversifier la recherche}, possibilité de faire des restarts à partir d'une nouvelle affectation initiale $A_0$

## min-conflicts

- Arrêt de l'algorithme quand une solution est trouvée ou quand un critère est atteint (p.ex. timeout)

- Possibilité de boucles dans la recherche, de rester bloqué dans des minima locaux

- Pas de garantie de trouver l'optimum

- \alert{Incapacité à trouver l'incohérence d'un problème}

## Recherche locale sur grands voisinages (LNS)

- choix d'une \alert{affectation initiale} $A_0$ quelconque, puis

- choix de $k$ variables $x_1, \ldots, x_k$ parmi les $n$ variables du problème

- \alert{recherche complète} de la meilleure réinstanciation de $x_1, \ldots, x_k$ étant donné les $n-k$ autres variables fixées à leur valeur courante (voisinage large)

- nouvelle affectation $A_{i+1}$ obtenue à partir de $A_i$ en donnant les meilleures valeurs trouvées à $x_1, \ldots , x_k$.

## Recherche locale sur grands voisinages (LNS)

Avantages:

- \alert{complexité limitée} de chaque recherche dans un voisinage large (complexité pire cas exponentielle en $k$ et non en $n$)
- par rapport à min-conflicts, plus de chance de \alert{sortir des optima locaux} (min-conflict $\equiv$ LNS avec $k = 1$)
- possibilité de \alert{faire varier $k$} pendant la recherche
- utilisation de la puissance des méthodes complètes sur des instances de taille ``raisonnable''

\alert{Paramètre à régler}: méthode de choix des $k$ variables à réinstancier à chaque étape

# Outils

## Solvers de contraintes

Plusieurs bibliothèques d'optimisation sous contraintes proposent:

- une API ou un langage de modélisation;
- des algorithmes de recherche et de propagation prédéfinis;
- des éléments pour paramétrer ces algorithmes;
- des éléments pour définir de nouvelles contraintes et de nouveaux types de branchements.

Parmi les plus célèbres: IBM ILOG CP Optimizer, Gecode, Choco, OR-Tools, etc.

Nous utiliserons dans les BE une interface Python pour un solver minimaliste libre et gratuit écrit en OCaml.
