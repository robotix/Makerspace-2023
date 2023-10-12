# Contribute to Makerspace-2023

We welcome the Makerspace-2023 participants to contribute, and we value everybody's contribution. Systematic contribution and version control is the key to a successful project. We have a few guidelines to help you get started with contributing to the project.

**This guide was heavily inspired by the awesome [Hugging Face Transformers Contributing Guidelines](https://github.com/huggingface/transformers/blob/main/CONTRIBUTING.md).**

## Ways to contribute

There are several ways you can contribute:

* Fix outstanding issues with the existing code.
* Submit a new feature or enhancement.
* Contribute to the examples or to the documentation.
* Improve the existing code quality or test coverage.

## Fixing outstanding issues

If you notice an issue with the existing code and have a fix in mind, feel free to [start contributing](https://github.com/robotix/Makerspace-2023/blob/main/CONTRIBUTING.md/#create-a-pull-request) and open a Pull Request!

## Adding documentation?

We're always looking for improvements to the documentation that make it more clear and accurate. Please let us know how the documentation can be improved such as typos and any content that is missing, unclear or inaccurate. We'll be happy to make the changes or help you make a contribution if you're interested!

## Create a Pull Request

Before writing any code, we strongly advise you to search through the existing PRs or
issues to make sure nobody is already working on the same thing. If you are
unsure, it is always a good idea to open an issue to get some feedback.

You will need basic `git` proficiency to contribute to this project. While `git` is not the easiest tool to use, it has the greatest
manual. Type `git --help` in a shell and enjoy! If you prefer books, [Pro
Git](https://git-scm.com/book/en/v2) is a very good reference.

You'll need **[Python 3.10](https://www.python.org/)** or above to contribute. Follow the steps below to start contributing:

1. Fork the [repository](https://github.com/robotix/Makerspace-2023) by
   clicking on the **[Fork](https://github.com/robotix/Makerspace-2023/fork)** button on the repository's page. This creates a copy of the code
   under your GitHub user account.

2. Clone your fork to your local disk, and add the base repository as a remote:

   ```bash
   git clone git@github.com:<your Github handle>/Makerspace-2023.git
   cd MakerSpace-2023
   git remote add upstream https://github.com/robotix/Makerspace-2023.git
   ```

3. Create a new branch to hold your development changes:

   ```bash
   git checkout -b a-descriptive-name-for-my-changes
   ```

   🚨 **Do not** work on the `main` branch!

4. Set up a development environment by running the following command in a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

 5. Develop the features on your branch.

   Once you're happy with your changes, add changed files with `git add` and
   record your changes locally with `git commit`:

   ```bash
   git add .
   git commit
   ```

   Please remember to write [good commit
   messages](https://chris.beams.io/posts/git-commit/) to clearly communicate the changes you made!

   To keep your copy of the code up to date with the original
   repository, rebase your branch on `upstream/branch` *before* you open a pull request or if requested by a maintainer:

   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

   Push your changes to your branch:

   ```bash
   git push -u origin a-descriptive-name-for-my-changes
   ```

   If you've already opened a pull request, you'll need to force push with the `--force` flag. Otherwise, if the pull request hasn't been opened yet, you can just push your changes normally.

6. Now you can go to your fork of the repository on GitHub and click on **Pull request** to open a pull request. Make sure you tick off all the boxes in our [checklist](https://github.com/robotix/Makerspace-2023/blob/main/CONTRIBUTING.md/#pull-request-checklist) below. When you're ready, you can send your changes to the project maintainers for review.

7. It's ok if maintainers request changes, it happens to our core contributors
   too! So everyone can see the changes in the pull request, work in your local
   branch and push the changes to your fork. They will automatically appear in
   the pull request.

### Pull request checklist

☐ The pull request title should summarize your contribution.<br>
☐ To indicate a work in progress please prefix the title with `[WIP]`. These are
useful to avoid duplicated work, and to differentiate it from PRs ready to be merged.<br>
☐ Make sure existing tests pass.<br>
☐ If adding a new feature, also add tests for it.<br>
☐ All public methods must have informative docstrings.<br>


### Style guide

For documentation strings, we follow the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html). 

For code style, we follow [PEP 8](https://www.python.org/dev/peps/pep-0008/). We use [autopep8](https://pypi.org/project/autopep8/) to format our code and [flake8](https://pypi.org/project/flake8/) to check for PEP 8 compliance. All code must be formatted with `autopep8` and pass `flake8` checks before being merged. Also use `isort` to sort imports.
