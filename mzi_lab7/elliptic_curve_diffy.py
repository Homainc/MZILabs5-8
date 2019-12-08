import random
from elliptic_curve import EllipticCurve

class AlgoDH:
    """ D.H's algorithm class  """

    def __init__(self, point):
        """ AlgoDH initilization """
        self.point = point
        for i in range(1, self.point.curve.p + 1):
            if self.point.x == 0 and self.point.y == 0:
                self.n = i
                break

    def get_public_key(self, private_key):
        """ Return the public key of D.H's algorithm """

        return self.point * private_key

    def encrypt(self, data_point, public_key, random_number):
        """ Encrypt the msg """

        return self.point * random_number, data_point + public_key * random_number

    def decrypt(self, data_point_pair, private_key):
        """ Decrypt the msg """

        return data_point_pair[1] + -(data_point_pair[0] * private_key)


# Example of encrypting and decrypting by D.H's algo
if __name__ == "__main__":

    # Elliptic curve initilization
    base_point = EllipticCurve(3, 345, 19).point_at(8)

    # Algo D.H. intitializing and private/public keys are created
    dh = AlgoDH(base_point)
    priv_key = random.randint(1, 100)
    pub_key = dh.get_public_key(priv_key)

    # Data is encrypted/decrypted by D.H. algorithm
    data = base_point * 2
    encrypted = dh.encrypt(data, pub_key, random.randint(1, 100))
    decrypted = dh.decrypt(encrypted, priv_key)
    print(decrypted == data)