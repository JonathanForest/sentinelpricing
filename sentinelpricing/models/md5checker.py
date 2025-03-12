import hashlib


# Python program to find MD5 hash value of a file
class MD5Checker:

    def __init__(self, file):
        self.file = file
        self.md5 = None

        if not self.file.closed:
            self.set_md5()
        else:
            raise ValueError("File Closed.")

        if self.md5 is None:
            raise RuntimeError()

    def __eq__(self, other):
        print(self.md5.hexdigest())
        return self.md5.hexdigest() == other

    def __ne__(self, other):
        return self.md5.digest() != other

    @classmethod
    def from_file(self, file):
        ...

    @classmethod
    def from_filepath(self, file):
        ...    

    def set_md5(self):
        
        if self.md5 is not None:
            raise AttributeError("Unable to write over md5.")

        md5_hash = hashlib.md5()

        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: self.file.read(4096), b""):
            md5_hash.update(byte_block)

        self.md5 = md5_hash
