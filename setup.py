from setuptools import setup, find_packages
setup(name='DT_app', version='0.0.1', description='Test excercise',
      packages=find_packages(),
      install_requires=['lxml==4.4.1',
                        'requests==2.21.0',
                        'waitress==1.3.1',
                        'flask==1.1.1',
                        'validators==0.14.0'
                        ]
      )
