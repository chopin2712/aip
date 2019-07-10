from distutils.core import setup
setup(
  name = 'aip',
  packages = ['aip'],
  version = '1.0',
  license='gpl-3.0', 
  description = 'Install all linux installers with only one command!',
  author = 'Chopin Dev',
  author_email = 'julien.lejoly2712@gmail.com',
  url = 'https://github.com/chopin2712/Auto-Installer-Process',
  download_url = 'https://github.com/chopin2712/aip/archive/v1.0.tar.gz',    # I explain this later on
  keywords = ['linux', 'auto', 'installer', 'process', 'install'],
  install_requires=[
          'fnmatch',
          'os',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: gpl-3.0',   # Again, pick a license
    'Programming Language :: Python :: 3.7',      #Specify which pyhton versions that you want to support
  ],
)
