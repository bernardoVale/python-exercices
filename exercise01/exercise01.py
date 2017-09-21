

def check_linux_version(kernel_info):

    if '.el6' in kernel_info:
        return 'el6'
    elif '.el7' in kernel_info:
        return 'el7'
    elif '.el5' in kernel_info:
        return 'el5'
    return 'unknown_version'
