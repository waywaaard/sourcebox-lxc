{
  "targets": [{
    "target_name": "lxc",
    "sources": [
      "src/lxc.cc",
      "src/async.cc",
      "src/get.cc",
      "src/attach.cc",
      "src/stop.cc",
      "src/destroy.cc",
      "src/clone.cc"
    ],
    "libraries": [
      "-lutil",
      "-llxc"
    ],
    "cflags": [
      "-std=c++11",
      "-Wpedantic"
    ],
    "include_dirs": [
      "<!(node -e \"require('nan')\")"
    ]
  }]
}
