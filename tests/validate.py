import os
import json
import yaml
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
recipe_path = os.path.join(project_dir, 'recipe.yml')
composer_path = os.path.join(project_dir, 'composer.json')

print(f"Checking {project_dir}...")

if not os.path.exists(recipe_path):
    print("FAIL: recipe.yml not found")
    sys.exit(1)

if not os.path.exists(composer_path):
    print("FAIL: composer.json not found")
    sys.exit(1)

try:
    with open(composer_path, 'r') as f:
        json.load(f)
    print("PASS: composer.json is valid JSON")
except Exception as e:
    print(f"FAIL: composer.json invalid: {e}")
    sys.exit(1)

try:
    with open(recipe_path, 'r') as f:
        yaml.safe_load(f)
    print("PASS: recipe.yml is valid YAML")
except Exception as e:
    print(f"FAIL: recipe.yml invalid: {e}")
    sys.exit(1)

print("ALL TESTS PASSED")
