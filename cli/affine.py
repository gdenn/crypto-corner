import click

from cipher.affine import Affine


@click.group()
def affine():
    pass


@click.command(name="encrypt")
@click.option("-m", "--msg", type=str, required=False, help="your plain text")
@click.option("-a", type=int, required=True, help="part of your key (gcd(a, k) != 1)")
@click.option("-b", type=int, required=True, help="part of your key")
@click.option("-f", "--file", type=str, required=False, help="(optional) msg from file")
def affine_encrypt(msg: str, file: str, a: int, b: int):
    cipher_txt: str = Affine.encrypt(file=file, msg=msg, a=a, b=b)
    print(cipher_txt)


@click.command(name="decrypt")
@click.option("-m", "--msg", type=str, required=False, help="your cipher text")
@click.option("-a", type=int, required=True, help="part of your key (gcd(a, k) != 1)")
@click.option("-b", type=int, required=True, help="part of your key")
@click.option("-f", "--file", type=str, required=False, help="(optional) msg from file")
def affine_decrypt(msg: str, file: str,  a: int, b: int):
    cipher_txt: str = Affine.decrypt(file=file, msg=msg, a=a, b=b)
    print(cipher_txt)


affine.add_command(affine_encrypt)
affine.add_command(affine_decrypt)
