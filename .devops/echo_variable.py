import yaml

def read_yaml_file(file_path):
    try:
        with open(file_path, 'r') as stream:
            config = yaml.safe_load(stream)
            return config
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: Unable to read file '{file_path}': {e}")
        return None

def get_variable_value(config, variable_name):
    if config is None:
        return None
    try:
        return config[variable_name]
    except KeyError:
        print(f"Error: Variable '{variable_name}' not found in config.")
        return None

def main():
    file_path = './config/test.yml'
    config = read_yaml_file(file_path)
    variable_value = get_variable_value(config, 'variable2')
    if variable_value is not None:
        print(variable_value)

if __name__ == '__main__':
    main()