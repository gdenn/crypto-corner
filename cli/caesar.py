import click

from cipher.caeser import Caesar


@click.group(name="caesar")
def caesar():
    pass


@click.command(name="encrypt")
@click.option("-m", "--msg", type=str, required=False, help="your plain text")
@click.option("-s", "--shift", type=int, required=True, help="alphabet shift (left direction)")
@click.option("-f", "--file", type=str, required=False, help="(optional) msg from file")
def caesar_encrypt(file: str, msg: str, shift: int):
    cipher_txt: str = Caesar.encrypt(msg=msg, file=file, shift=shift)
    print(cipher_txt)


@click.command(name="decrypt")
@click.option("-m", "--msg", type=str, required=False, help="your cipher text")
@click.option("-s", "--shift", type=int, required=True, help="alphabet shift (right direction)")
@click.option("-f", "--file", type=str, required=False, help="(optional) msg from file")
def caesar_decrypt(file: str,msg: str, shift: int):
    plain_txt: str = Caesar.decrypt(msg=msg, file=file, shift=shift)
    print(plain_txt)


caesar.add_command(caesar_encrypt)
caesar.add_command(caesar_decrypt)
