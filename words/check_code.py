#!/usr/bin/env python3
import re, sys, glob, hashlib

def main():
    with open("words.c") as f:
        text = f.read()

    allowed_numbers = ["0", "1", "13", "14"]

    identifiers = re.findall("[_a-zA-Z][_a-zA-Z0-9]*", text)

    if "scanf" not in identifiers:
        print("ERROR: The function scanf has not been used.")
        sys.exit(1)

    for too_small_array in re.findall(r"char +[a-zA-Z_0-9]+\[13\]", text):
        print(f'The array "{too_small_array}" is too small to fit the null terminator.')
        sys.exit(1)

    if 'scanf("%s' in text:
        print('"%s" is an unsafe format string for scanf. The length should always be limited.')
        sys.exit(1)

    for number in re.findall(r"^[a-zA-Z_]\d+", text):
        if number not in allowed_numbers:
            print(f"ERROR: The number {number} was used. "
                f"Only the numbers {', '.join(allowed_numbers)} are allowed")
            sys.exit(1)

    hashes = set(['5a6fefc939e3765107c0c708686922cbc8d943ff99fd1f036e4f439f8284a0b4', 'ae7e6456ab7a3b6b78bd1054aa8b75e3e1f920f95a687b717d51dade6e1b7b12', '8044d3d5bc91573fc3e8602ae8b0472619079f97acc19f420309b754ff012c21', 'd437f0cd52749a6ebef277ba54ea12dd35041b8ba3d35c84603a65bd54d7eb72', '424f45447d9ec292025b034e654dc4dfcbf23915f3e0c1e6086e534af9bd94ca', '167a729d43e19d318a52a3262fb8485b3fe1baa030f3c00312158016fb15b46f', '15bb41475f7a86ee0477744dd61e9e8eee6100997703bca03e0350321e229249', '18cb556bcdc864b326fc0e4c3aba12d98e91ff188909134c6f69d0a2f1661dea', '1b720fabdc856abec3aa19b5cb90532b2310cfd3c126d0f2e4164c8af6e7bd54', '3839a7580ab8080cf89852ba1d164f7e5729edbe7d6c811f742b91426cd66777', 'e3d33db3143a85cc7eba0a27ccf4d19295de0de80fbd55cad8bcef6c5ada554e', 'f167ed7e07d25633303afff1450d62840d3e5aa62d7ae117e39ca651354876f8', '8bb74f3a31786a849d84c0c5523c4084165d2c957aeb9e4738e967e096cfd741', '3c7dbdbcb872b3e9cbef2e3e9ea2fc1a6124880d4db1f772f5213be00822fd85', '584aa2478543eba046dee15a2999ba1c36f99a9dee07efbc9d53b5a35acee17a', 'ad91bf426ce69345df3d75ff65ceee0d47146a1ae5430b3c3d53d3932a8fffda', 'e6d0f8bdcd85825cdd84f09e52e30943d336c3ce8a2699bd151f1714b9e769ea', '7c3ccede4081e6846938edb3a32ad159285f5f8a036e3aa5485017a024433144', 'd533710d33a71fbdf3b22fa7811b2bc161c46d7e6907cf47959a5050f6ae7a37', 'f6eb1b22a50bcc0cdcd6835c044daf2d6efe55c330ab91565d3b6fb0893db5ae', '097bc7d476385bb3f6b2ca2291308e4f330ef7bc2b6e730a51706fe34672c7cd', 'ca7c7ba1e805c30f4a70c55f2955388ff5d8bb54707f70b485ecf1fe6ae2fc06', '242ff57deac890c355d9685cd0079292eaaf5ca3e17de5af9166a14a7671341b', '225b82bee1d2337672e78a235219ce1502ab4c87a4356be9f16a67fec021dab9', '643dee008bd2d33a9400923bb409b0b25c383284df52e0a4e3dc1391bcf18ff3', '8c3d1a2c2e8d17a43aa894942a161114c61d8031295d113d9615ba4e072e1cf5', '99eb58b5647dd44f73dcdbcb875b6bc83890d09e0a369a89c1a1343c462e2703', '26a1c641819c9854d2ef2f1f0181f4f5e58e6b207449585fbed51be536c95251', 'c36c8a99688c6eb3486eac8a4d0548a5d683fa43deb9c73be7efd57bf72ebf30', 'ad4fc4b28701a32e8b75e7db1af8159f42effc98d25a17b06dcb5a0f78869249', '5a34f383d2135c2b70f646e8c8b15839e3300033b894e6a5eb6382971d3edb84', '2cac545bd77946bc40278d1adfba5a1cf989d153ad649afc57a8e2f9c209a586', '5f0dea5ec5a54f65bb4cf0b529832135b684dc9ef9756e93d82a107e5800ed52', '333ccd91920b5e071539f5bda64cfb730aac7cf3d61d188039623ce3246d1178', '08fb0ddf5f703e9bd2acfcdb4758c513a0c57dbd0aad0609a0512cd0355ae2a1', '347d5ade313488b68a900d10ddf4b157613c905f40e3ee212f7d9754b40a79e2', '9a3e62b1952168816a01db1e25d890fc4ec130015f9264fd234dc0cf4f37247d', '50eba4d61065ec99e826c1736e6f52644e19921f160a9f975685cf4dfb3db0a7', 'e97d77ae3e879b8f7234278c21cde4e8eeabc6494135a21e1499950ce01e6a32', '504881a2f8063289063f5f656b456f11b15a7ab732128652d773f37e6d334557', 'e84ccbce26aca15a5e3581953d99addcaaf6621cf3b31b7a4f5879bb8cd89ffb', '05e52ccc4fc316edb78dce2d7d392f2aba1b16fdd7f2884b85fa5e9f7bbfe48c', 'a673085895cc1027e5635fbda5bc4fc5f9daeca56b6b0b18de05a4e63df859ed', 'faa8b5f72d9081371c7aad162729dd5996db1ec4ea316e75bd4d12e2e59ce9f1', '92a5d4744dc7cb21cf1f22c41d1f5345920a71ac0d41cb4f86b1e2ff88f32851', '63525ee82d77aefee67607c811f945c6074e0f13845a1bcd6f22a1be0cd090fb', '6891c132c3eb8dfc0bf317e673670d5a31acacede9c9f31413b28226eb6294da', 'df63b096183e41e34a1a6a0efe65e0f66a6b532cf6321dc11cc157a113fd766e', '55be88142d49428cf1949202dad4a3a9dab77034c214707dea1f5012105ff0d9', '1a963538d7da524c4a84f12b58124ccff0e8ae0708158c99253fe1446a5cfea1', '64410dc7109b69bf40a78614b95f1750dc65abb1a8ba16c74f71f7a170558f12', '71c9df6d65f87d42e6e7ce35d651248d671f2d699b923d282362299a8359c9c0', '551cf98e1136152c88e491d3483f2abac2bc0a674bf72d5b33d4254b55c7708c', 'e58b54f53434168fe03ca2dadea63eca3d3448f2245133d4e2a109d9ef687e1b', '8ccfcf0153a3ff8e3ec75a8861d5116825c484cbeaeab114cc2225c27c84db31', 'e8ea7eacf21c8bcc78df99f5924c0c60ccb4332922001b9b3e28aab9dd141c8a', '2c0ab39ccd257b40a0dbf532ff2d38dd1125843b7ee1fbfbcd5275108111ca21', '6eeca6238cecc558c2f393fb80b50e867ed6633d173b5e736df3b49c9c0df80a', '3a5dd4e38fb0ce5cc6abeeb0fb85befdaa1df956de9c77178d9d20cfc01a3b56', '9387c77991057f3ea4b9554a92fbb622c650c4ce201b3176362ebcce7145af93', '22844795afd1e5196b34def9bab6dae586384a8bbc50c119c3c4fd9b69ed7bc6', '05e5b9a952d8c2d9e0a041dd60c2c841c2b3f67f2099dcf9c51e9ccf8d162285', 'e3b0d401736ca311edb1417f0981959ecb4e415d79d392fa35e22e97663c7de7', '3e6c5caf4cdaebf0f6158efe7ca84ec9dbdc0719baef810bfba72a37907a1232', 'b96fb479bfcaf3ea8da2fed6ecae950d85d99d4dbdfec2c9a77b598106153bb3', 'dc0fe7d29b10c678bf642449d635c491a8f97ee16b5ebdfece5f7e3d65d1e4e5', '0fe69531670ddbda86d021560a5d78a142d5d76d2c4dcd220a54e5bfd10ffd2c', 'e944a6a6cccf59784747b5a5454f3aeaa56de87c59d9e323fca7d0494ae1b842', '7bf0234afa90add529e43fa8fe47e2ecdbd4d050f2ef37618b6324236a10b125', '92cb4fa814b9bf2cbb8d0fa228a7bffe28f670442d08b2508e1cd1f4cb257358', 'f3cb8b9d8fcc3ec99a3d9f230dc2b3a56485abd742a556220964b1c935aaa435', '5394420befc1ab3af985400d45dbfea5c285bc36bb509e4b046c290152578904', 'c7b5a5e9fb8675490a36341c2b9dd293ebfec8b5ce05106dbe49fb71377e351a', '0d11827aba86f1c259ea91d31941772bf3c8b8894b9fad6420635b736a689b05', '4f4232d7c928201e990dc73d718c51d97c25542633179811ae56948e9414d626', '526cd6cd67d01905c6b7613a30fe45f6f79b4e53f9789e081db619c6112e8bca', 'cf29d20c5e18352c1d5a3957cbc2a5cc054b547bed17e8adb29f46e8661daad2', '89168b1b36bbce57a4d776090235ed8b8eefcab926e9671459da8bd3da4a7f37', '5c6852e617bc30847c9b23497faa810b0b4189c75f22c03bb6d77e1b4173937f', '6b229d8e7b6410b1174ab7103f188124787e3861cd2ca4b0082d7b8fe114179a', '50335955ebf98c029b2d500ad38e01c838c3484b24403b27bd694e9d3f851099', '8c5ef556eb30bd30ee0dbd30c7be0d033a3ddf0b879e75b0b779e264c9417ba3', '93812b82432ff8382177a6b95d03c247178b529945ce3df346a6cbc8081d3b5b', 'f69ec2d799b8a3fadffde79ffc63143a6f21816dd08aa4564fba5025095bccdd', 'f94bd64f396b80f9d6a7fb578450cbb930531601a09b79cf4eb2dca01cd0df7c', '41d8aaaf2c197de87783f4854a2a4c2abbe9278d8144f869b9187660a71dfc1e', '5855ca6468ea29b28eac8bf1ef841664cfbcbd16a0948505aa2234eae54ed21b', 'a37ce6f8848e669fa4ed4aac38b058a320bd34043b00b0355b0516a089170b40', '1e6151b739fee0ed71dc4c8089361b2fb25214a8ac75f6024bc1884c09ff6268', 'f2f132343179a4b4871d5eab58a23b047cdd53de45c97230b82caa008ac2d146', '957f5801d15563e14b9896d58b652de1885c498211898d1f7a90464055871a10', 'a42b113e345961bf6bbaf75cdb3f9e0c23097d97e10cb4258e771766a1e4d90d', '30c65345e2b3c70b3112ca5afe9cf27c1d9ef2a3f7229827b8a2aefca4749ff9', '3ce6f2cfe7b40ff613806f0832e6351ae09ada3f3b2a1515435052f19567fa07', '148030ab913729bc857685f5917385a1880d4e42cd3907130e0811ca8ade8bfe'])
    for path in glob.iglob("**/*.c", recursive=True):
        with open(path, encoding="utf-8") as f:
            for line in f.read().split("\n"):
                h = hashlib.sha256(line.strip().encode("utf-8")).hexdigest()
                if h in hashes:
                    try:
                        with open("output5.txt") as f:
                            lines = f.read().split("\n")
                    except FileNotFoundError as e:
                        lines = []
                    with open("output5.txt", "w") as f:
                        f.write("\n".join(set(lines + [h])))


if __name__ == "__main__":
    main()
