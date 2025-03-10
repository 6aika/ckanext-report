from setuptools import setup, find_packages

version = '0.1'

setup(
    name='ckanext-report',
    version=version,
    description="Framework for defining reports in CKAN",
    long_description='''
    ''',
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='David Read',
    author_email='david.read@hackneyworkshop.com',
    url='',
    license='Affero General Public License',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        report = ckanext.report.plugin:ReportPlugin
        tagless_report = ckanext.report.plugin:TaglessReportPlugin

        [paste.paster_command]
        report = ckanext.report.command:ReportCommand
        
        [babel.extractors]
        ckan = ckan.lib.extract:extract_ckan
    ''',
    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    }
)
