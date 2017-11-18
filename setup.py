from setuptools import setup, find_packages

VERSION = "1.0.1"

setup(name="singlepy",
      version=VERSION,
      author="Alessio Linares",
      author_email="alessio@alessio.cc",
      description=("Small library that offers two simple to use singleton-pattern metaclasses: "
                   "Singleton and WeakSingleton"),
      keywords=["singleton"],
      url="https://github.com/Galbar/singlepy",
      download_url="https://github.com/Galbar/singlepy/archive/{}.tar.gz".format(VERSION),
      license='MIT',
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 5 - Production/Stable',

          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries',

          # Pick your license as you wish (should match "license" above)
          'License :: OSI Approved :: MIT License',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      python_requires='>=3.4',
      packages=find_packages(exclude=["tests"]))
