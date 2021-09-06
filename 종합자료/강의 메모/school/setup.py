
from setuptools import setup, find_packages

setup(
    name = 'dss',
    packages=find_packages(),
    include_package_data=True, # 패키지 데이터를 모두 포함시킨다.
    version='0.0.1',
    author_email='todaybow@naver.com',
    zip_safe=False,    
)
