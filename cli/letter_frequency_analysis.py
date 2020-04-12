import click

from attack.letter_frequency_analysis import LetterFrequencyAnalysis


@click.group()
def letter_frequency():
    pass


@click.command(name="analyze")
@click.option("-m", "--msg", type=str, required=False, help="your cipher text")
@click.option("-l", "--language", type=str, required=False, default="en", help="which language (en/de)")
@click.option("-f", "--file", type=str, required=False, help="(optional) msg from file")
def analyze(msg: str, file: str, language: str):
    LetterFrequencyAnalysis.decrypt(file=file, msg=msg, lan=language)


letter_frequency.add_command(analyze)
