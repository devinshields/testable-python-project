#!/usr/bin/env python
'''  '''

def string_repeater(any_string):
    ''' function repeats any string you throw at this baby. twice. '''
    return any_string + any_string


def main():
  some_string = 'Goooooooooooooooooooood morning vietnam!'
  repeated_string = string_repeater(some_string)
  print '\nsome_string: {}\nrepeated_string: {}\n'.format(some_string, repeated_string)


if __name__ == '__main__':
  main()

