import click

from cipher.caeser import Caesar


@click.group(name="caesar")
def caesar():
    pass


@click.command(name="encrypt")
@click.option("-m", "--msg", type=str, required=True, help="your plain text")
@click.option("-s", "--shift", type=int, required=True, help="alphabet shift (left direction)")
def caesar_encrypt(msg: str, shift: int):
    cipher_txt: str = Caesar.encrypt(plain_txt=msg, shift=shift)
    print(cipher_txt)


@click.command(name="decrypt")
@click.option("-m", "--msg", type=str, required=True, help="your cipher text")
@click.option("-s", "--shift", type=int, required=True, help="alphabet shift (right direction)")
def caesar_decrypt(msg: str, shift: int):
    plain_txt: str = Caesar.decrypt(cipher_txt=msg, shift=shift)
    print(plain_txt)


caesar.add_command(caesar_encrypt)
caesar.add_command(caesar_decrypt)
