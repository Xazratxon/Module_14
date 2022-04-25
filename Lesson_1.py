import platform
import sys

info = 'OS info is \n{}\n\nPython version is {} {} {}'.format(
    platform.uname(),
    sys.version,
    platform.architecture(),
    'сельдерей ююююрейй',
)


print(info)

with open('os_info.txt', 'w', encoding='utf8') as file:
    file.write(info)
