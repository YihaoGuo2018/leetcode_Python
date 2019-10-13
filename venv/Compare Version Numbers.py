class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def compareVersion(self, version1, version2):

            version1arr = version1.split('.')
            version2arr = version2.split('.')

            lengthdiff = len(version1arr) - len(version2arr)
            if lengthdiff > 0:
                for i in range(lengthdiff):
                    version2arr.append(0)
            if lengthdiff < 0:
                for i in range(-lengthdiff):
                    version1arr.append(0)

            for i in range(len(version1arr)):

                if int(version1arr[i]) > int(version2arr[i]):
                    return (1)
                elif int(version1arr[i]) < int(version2arr[i]):
                    return (-1)
            return 0

