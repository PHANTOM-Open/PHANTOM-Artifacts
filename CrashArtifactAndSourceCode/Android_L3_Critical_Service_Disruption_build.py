import os
import subprocess
from multiprocessing import get_context

def gen_keystore(i):
    cmd=f"yes |keytool -genkeypair -keystore {str(i).rjust(4,'0')}.keystore -alias {str(i).rjust(4,'0')} -keyalg RSA -keysize 2048 -storepass android -validity 10000"
    print(cmd)
    subprocess.run(cmd, shell=True, env=os.environ, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == '__main__':
    with get_context("spawn").Pool() as p:
        for i in range(1410):
            if(os.path.isfile(f"{str(i).rjust(4,'0')}.keystore")):
                continue
            p.apply_async(gen_keystore, args=(i,))
        p.close()
        p.join()

    cmd = 'apksigner sign --ks 0001.keystore --ks-key-alias 0001 --ks-pass pass:android '
    for f in os.listdir("./"):
        if f.endswith(".keystore"):
            idx = f.split(".keystore")[0]
            if idx == '0001':
                continue
            cmd += f'--next-signer --ks {idx}.keystore --ks-key-alias {idx} --ks-pass pass:android '
    cmd += '--v3-signing-enabled=false --out new.apk app-debug.apk'
    print(cmd)
    os.system(cmd)
    # apksigner verify --print-certs new.apk
        