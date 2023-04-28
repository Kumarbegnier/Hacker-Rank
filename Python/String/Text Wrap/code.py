import textwrap


def wrap(string, max_width):
    # Wrap the given string into multiple lines of given width
    wrapped_text = textwrap.wrap(string, max_width)
    
    # Join the wrapped lines with '\n' separator and return the resulting string
    return '\n'.join(wrapped_text)


if __name__ == '__main__':
