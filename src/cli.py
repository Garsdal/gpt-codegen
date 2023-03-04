import click, json, os
from src import _SRC_DIR

@click.group()
def cli():
    pass


@click.command()
@click.option("--key", type=str, help="OpenAI API key")
def config_api(key):
    config = {"API_KEY": key}
    if (key is None) or (key == ""):
        click.echo("Please provide a valid API key")
        return
    
    config_path = os.path.join(_SRC_DIR.parent, "config")
    if not os.path.exists(config_path):
        os.mkdir("config")

    try:
        config_file = os.path.join(config_path, "config_api.json")
        with open(config_file, "w") as f:
            json.dump(config, f)
    except Exception as e:
        click.echo(f"Error occurred: {e}")
        return
    

cli.add_command(config_api)

if __name__ == "__main__":
    cli()