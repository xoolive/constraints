# Constraint programming

This is a short course about constraint programming.

## Materials

- a tl;dr [introduction](https://github.com/xolearn/constraints/blob/master/documents/summary.pdf) with the bare minimum to know about constraint programming;
- [slides](https://github.com/xolearn/constraints/blob/master/documents/slides.pdf) for a 3h course, pdf version

## Environment setup

<div class="alert alert-warning">
<b>Windows users</b> should first activate WSL using the official <a href="https://docs.microsoft.com/en-us/windows/wsl/install-win10">instructions</a> (<a href="https://docs.microsoft.com/fr-fr/windows/wsl/install-win10">French version</a>). Please install the most recent Ubuntu version (unless you have another version ready.)
</div>

You will need to set up **by yourself** the following pieces:

- [Visual Studio Code](https://code.visualstudio.com/), then install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python):

  ```sh
  code --install-extension ms-python.python ms-toolsai.jupyter
  ```

  **Windows users** should also activate the Remote WSL extension:

  ```sh
  code --install-extension ms-vscode-remote.remote-wsl
  ```

- an Anaconda distribution, from the [following link](https://www.anaconda.com/products/individual). In case the question arises, it is very likely that the best suited version for your needs is the 64 bits one. Anaconda is more than a Python distribution: it also provides additional dependencies you may need;

  **Windows users** should install the anaconda distribution on their Linux subsystems.

- the `git` (or `git.exe` for Windows users) program, for version control. Using Git falls out of scope of this seminar, but you are **strongly encouraged** to become proficient with it. You may find resources on [GitHub Learning Lab](https://lab.github.com/), e.g. the following course for [first-timers](https://lab.github.com/lmachens/git-and-github-first-timers).

  Try running `git --version`. If necessary, install `git`:

  | Operating system | Installation command   |
  | ---------------- | ---------------------- |
  | MacOS            | `brew install git`     |
  | Linux (Ubuntu)   | `sudo apt install git` |

- clone the resources for the course:

  ```sh
  git clone https://github.com/xoolive/constraints
  ```

  **Windows users** should install the dependencies within their Ubuntu subsystem

  You may move the folder at any time if you prefer to keep things sorted differently on your computer.

- install the dependencies

  ```sh
  cd constraints
  pip install -r requirements.txt
  ```

## Lab session

A self-documented notebook is available in the notebook folder. The free and open-source `facile` library is a basic wrapper around the OCaml `facile` solver. You may find more powerful solvers in your future life but this one should do the job to introduce and illustrate the basic concepts of constraint programming in Python.

The notebook for the basic lab session is `notebook/lab-session.ipynb`.

Run the following command (in WSL for **Windows users**):

```sh
jupyter lab
```

## Project

Projects should be run as Python scripts from Visual Studio Code.

Open the workspace file (with the WSL connector for **Windows users**), then access the project folder.

Details about projects are presented on this [page](/constraints/problems).

### Troubleshooting

In case you are stuck with your configuration for the first lab session **only**, you can fall back to a slightly less comfortable option with [Google Colab](https://colab.research.google.com/github/xolearn/constraints/blob/master/notebooks/lab_session.ipynb):

- click on the [link](https://colab.research.google.com/github/xolearn/constraints/blob/master/notebooks/lab_session.ipynb);
- insert a new cell at the top of the notebook with

  ```sh
  !pip install 'facile>=1.5'
  ```

  and execute it to install the library;

- all the `%load` commands for the solutions will not work: you will have to copy paste the solutions directly from each of these files.

## Further reading

- _Constraint Processing_ (book) by Rina Dechter
- [Le problème des 8 reines... et au-delà](https://tinyurl.com/8reines) par Jean-Paul Delahaye.
  Pour la science, janvier 2016
