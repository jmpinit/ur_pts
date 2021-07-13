import sys
import chevron
import socket

poses = [
  [0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.1, 0.1, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.1, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
]

if __name__ == '__main__':
  host = sys.argv[1]
  port = 30002

  with open('ur_script/template.urscript', 'r') as template_file:
    named_points = []

    for i in range(len(poses)):
      pose = poses[i]
      ending = ',' if i < len(poses) - 1 else ''
      named_points += [{ 'pose': f'{str(pose)}{ending}' }]

    ur_program = chevron.render(template_file, {'points': named_points})

    print(f'Sending program to {host}:{port}')
    print(ur_program)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.connect((host, port))
      sock.send(ur_program.encode('utf-8'))

