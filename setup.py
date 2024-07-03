import sys
import subprocess
from setuptools import setup, find_packages
from distutils.core import Command

VERSION = "1.2.2"

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

class DistWheelCommand(Command):
	"""Custom command to ensure all changes are committed or stashed, and build sdist and bdist_wheel."""
	
	description = "Check for local changes, stash them, run sdist and bdist_wheel, then pop the stash"
	user_options = []

	def initialize_options(self):
		pass

	def finalize_options(self):
		pass

	def run(self):
		# Check if there are uncommitted changes
		result = subprocess.run(['git', 'status', '--porcelain'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		if result.returncode != 0:
			print("Error running git status")
			sys.exit(1)
		
		if result.stdout:
			print("You have uncommitted changes:")
			print(result.stdout.decode())
			response = input("Would you like to stash these changes and proceed with the build? [y/N]: ").strip().lower()
			if response == 'y':
				# Stash changes
				stash_result = subprocess.run(['git', 'stash', '--include-untracked'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				if stash_result.returncode != 0:
					print("Error stashing changes")
					sys.exit(1)
				stash_applied = True
			else:
				print("Please commit or stash your changes before building the package.")
				sys.exit(1)
		else:
			stash_applied = False
		
		try:
			# Run the original sdist and bdist_wheel commands
			self.run_command('sdist')
			self.run_command('bdist_wheel')
		finally:
			if stash_applied:
				# Reapply the stash
				stash_pop_result = subprocess.run(['git', 'stash', 'pop'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				if stash_pop_result.returncode != 0:
					print("Error popping stash")
					sys.exit(1)

setup(
	name="laundrify_aio", 
	version=VERSION,
	author="Mike Mülhaupt",
	author_email="mike@laundrify.de",
	cmdclass={
		'dist_wheel': DistWheelCommand,
	},
	license="MIT",
	url="https://github.com/laundrify/laundrify-pypi",
	description="A Python package to communicate with the laundrify API",
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=find_packages(),
	install_requires=["aiohttp", "pyjwt"],        
	keywords=["home-assistant", "laundrify"],
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.7",
		"Intended Audience :: Developers"
	],
)