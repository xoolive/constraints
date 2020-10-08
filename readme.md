# Constraint programming

This is a short course about constraint programming.

## Materials

- a tl;dr [introduction](https://github.com/xolearn/constraints/blob/master/documents/summary.pdf) with the bare minimum to know about constraint programming;
- slides for a 3h course, pdf version

## Lab session

A self-documented notebook is available in the notebook folder. The free and open-source `facile` library is a basic wrapper around the OCaml `facile` solver. You may find more powerful solvers in your future life but this one should do the job to introduce and illustrate the basic concepts of constraint programming in Python. 

You will need a working Python environment. Anaconda is recommended. To access the materials:
```sh
pip install facile
git clone https://github.com/xolearn/constraints
jupyter lab
```

The notebook for the basic lab session is `notebook/lab-session.ipynb`.

### Troubleshooting

In case you are stuck with your configuration, you can fall back to a slightly less comfortable option with [Google Colab](https://colab.research.google.com/github/xolearn/constraints/blob/master/notebooks/lab_session.ipynb):

- click on the [link](https://colab.research.google.com/github/xolearn/constraints/blob/master/notebooks/lab_session.ipynb);
- insert a new cell at the top of the notebook with  
  ```
  !pip install facile
  ```  
  and execute it to install the library;
- all the `%load` commands for the solutions will not work: you will have to copy paste the solutions directly from each of these files.

## Project

Several projects are available in the `problems/` folder. You will be evaluated on one of the projects available there. Obviously, these notebooks do not contain any hint or solution.

## Further reading

- *Constraint Processing* (book) by Rina Dechter
- [Le problème des 8 reines... et au-delà](https://tinyurl.com/8reines)  par Jean-Paul Delahaye.  
  Pour la science, janvier 2016