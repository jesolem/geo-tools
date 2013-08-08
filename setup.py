from setuptools import setup

setup(name='geo-tools',
      version='0.1',
      description='Collection of geo tools',
      author='Jan Erik Solem',
      url='https://github.com/jesolem/geo-tools',
      packages=['gh_geojson', 'geo_exif', 'geocoding'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
      ])