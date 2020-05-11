from flask import Blueprint, request
from Crypto.Util.number import getPrime
from Crypto.PublicKey import RSA


blueprint = Blueprint('getkeyz', __name__)

d = {
    "31d487ee7d1557762badf6c3304cdf96": 254237018189625576360550658485620926581 * 331022516054965003695518217900122313193
}

@blueprint.route('/kitty')
def get_key():
    hostname = request.args.get('hostname')
    print(hostname)
    if hostname not in d:
        d[hostname] = getPrime(128) * getPrime(128)
    n = d[hostname]
    # print(n)
    v = RSA.construct((n, 65537)).exportKey()
    # zz = RSA.importKey(v)
    # print(zz.n)
    return v