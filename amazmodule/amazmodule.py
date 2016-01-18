#!/usr/bin/env python
'''  '''

def string_repeater(input_string):
    ''' function repeats any string you throw at this baby. twice. '''
    if not isinstance(input_string, basestring):
        raise TypeError('input_string must be of string type!')
    if not len(input_string):
        raise ValueError("You can't repeat an empty string, you silly goose!")
    return input_string + input_string


def main():
  input = 'Goooooooooooooooooooood morning vietnam!'
  output = string_repeater(input)
  print '\ninput:  {}\noutput: {}\n'.format(input, output)


if __name__ == '__main__':
  main()

