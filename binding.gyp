{
  'targets': [
    {
      'target_name': 'imagick',

      'variables': {
        'wand-config': 'Wand-config',
      },
      'sources': [
        'src/imagick.cc',
        'src/command.cc',
      ],
      'cflags': [
        '<!@(<(wand-config) --cppflags)',
      ],
      'libraries': [
        '<!@(<(wand-config) --libs)',
      ],
      'ldflags': [
        '<!@(<(wand-config) --ldflags)',
      ],
      'xcode_settings': {
        'OTHER_CFLAGS': [
          '<!@(<(wand-config) --cppflags)',
        ],
        'OTHER_LDFLAGS': [
          '<!@(<(wand-config) --ldflags)',
        ],
      },
    }
  ]
}
