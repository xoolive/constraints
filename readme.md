# Constraint programming

This is a short course about constraint programming.

## Materials

- a tl;dr [introduction](https://github.com/xolearn/constraints/blob/master/documents/summary.pdf) with the bare minimum to know about constraint programming;
- [slides](https://github.com/xolearn/constraints/blob/master/documents/slides.pdf) for a 3h course, pdf version

## Lab session

A self-documented notebook is available in the notebook folder. The free and open-source `facile` library is a basic wrapper around the OCaml `facile` solver. You may find more powerful solvers in your future life but this one should do the job to introduce and illustrate the basic concepts of constraint programming in Python.

You will need a working Python environment. Anaconda is recommended. To access the materials:

```sh
git clone https://github.com/xolearn/constraints
cd constraints
pip install -r requirements.txt
jupyter lab
```

The notebook for the basic lab session is `notebook/lab-session.ipynb`.

### Troubleshooting

In case you are stuck with your configuration, you can fall back to a slightly less comfortable option with [Google Colab](https://colab.research.google.com/github/xolearn/constraints/blob/master/notebooks/lab_session.ipynb):

- click on the [link](https://colab.research.google.com/github/xolearn/constraints/blob/master/notebooks/lab_session.ipynb);
- insert a new cell at the top of the notebook with

  ```sh
  !pip install 'facile>=1.5'
  ```

  and execute it to install the library;

- all the `%load` commands for the solutions will not work: you will have to copy paste the solutions directly from each of these files.

## Project

More details on this [page](/constraints/problems).

## Further reading

- _Constraint Processing_ (book) by Rina Dechter
- [Le problème des 8 reines... et au-delà](https://tinyurl.com/8reines) par Jean-Paul Delahaye.  
  Pour la science, janvier 2016
