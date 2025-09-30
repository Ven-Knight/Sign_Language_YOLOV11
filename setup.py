from setuptools import find_packages, setup

setup(
        # ---------------------------------------------------------
        # Project metadata for PyPI or internal distribution
        # ---------------------------------------------------------
        name             = 'Sign Language Detection',             
        version          = '0.0.0',
        author           = 'Venkat Reddy Nalamalapu',
        author_email     = 'venkatareddy.nalamalapu@gmail.com',

        # ---------------------------------------------------------
        # Package discovery — auto-detects all Python modules
        # ---------------------------------------------------------
        packages         = find_packages(),                       # Includes all submodules with __init__.py

        # ---------------------------------------------------------
        # Dependency list — populate as pipeline evolves
        # ---------------------------------------------------------
        install_requires = []                                     # Add runtime dependencies here (e.g., opencv-python, torch)

     )