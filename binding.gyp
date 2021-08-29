{
  "targets": [{
    "target_name": "leveldown",
    "conditions": [
      ["OS == 'win'", {
        "defines": [
          "_HAS_EXCEPTIONS=0"
        ],
        "msvs_settings": {
          "VCCLCompilerTool": {
            "RuntimeTypeInfo": "false",
            "EnableFunctionLevelLinking": "true",
            "ExceptionHandling": "2",
            "DisableSpecificWarnings": [ "4355", "4530" ,"4267", "4244", "4506" ]
          }
        }
      }],
      ["OS == 'linux'", {
        "cflags": [],
        "cflags!": [ "-fno-tree-vrp"]
      }],
      ["OS == 'mac'", {
        "cflags+": ["-fvisibility=hidden"],
        "xcode_settings": {
          # -fvisibility=hidden
          "GCC_SYMBOLS_PRIVATE_EXTERN": "YES",

          # Set minimum target version because we're building on newer
          "MACOSX_DEPLOYMENT_TARGET": "10.10",

          # Build universal binary to support M1 (Apple silicon)
          "OTHER_CFLAGS": [
            "-arch x86_64",
            "-arch arm64"
          ],
          "OTHER_LDFLAGS": [
            "-arch x86_64",
            "-arch arm64"
          ]
        }
      }],
      ["OS == 'android'", {
        "cflags": [ "-fPIC" ],
        "ldflags": [ "-fPIC" ],
        "cflags!": [
          "-fno-tree-vrp",
          "-mfloat-abi=hard",
          "-fPIE"
        ],
        "ldflags!": [ "-fPIE" ]
      }],
      ["target_arch == 'arm'", {
        "cflags": [ "-mfloat-abi=hard" ]
      }]
    ],
    "dependencies": [
      "<(module_root_dir)/deps/leveldb/leveldb.gyp:leveldb"
    ],
    "include_dirs"  : [
      "<!(node -e \"require('napi-macros')\")"
    ],
    "sources": [
      "binding.cc"
    ]
  }]
}
