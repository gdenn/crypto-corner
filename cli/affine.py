import click

from cipher.affine import Affine


@click.group()
def affine():
    pass


@click.command(name="encrypt")
@click.option("-m", "--msg", type=str, required=True, help="your plain text")
@click.option("-a", type=int, required=True, help="part of your key (gcd(a, k) != 1)")
@click.option("-b", type=int, required=True, help="part of your key")
def affine_encrypt(msg: str, a: int, b: int):
    cipher_txt: str = Affine.encrypt(msg=msg, a=a, b=b)
    print(cipher_txt)


@click.command(name="decrypt")
@click.option("-m", "--msg", type=str, required=True, help="your cipher text")
@click.option("-a", type=int, required=True, help="part of your key (gcd(a, k) != 1)")
@click.option("-b", type=int, required=True, help="part of your key")
def affine_decrypt(msg: str, a: int, b: int):
    cipher_txt: str = Affine.decrypt(msg=msg, a=a, b=b)
    print(cipher_txt)


affine.add_command(affine_encrypt)
affine.add_command(affine_decrypt)
