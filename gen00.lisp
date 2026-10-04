;; Overview diagrams for https://plops.github.io
;;
;; Pipeline (run from the repo root):
;;   sbcl --non-interactive --load gen00.lisp --quit   ; gen_graphviz.py + index.html
;;   uv run python gen_graphviz.py                     ; graph0..N.svg
;;   sbcl --non-interactive --load gen00.lisp --quit   ; index.html with fresh SVGs
;;
;; The *graphs* section below is generated, do not edit by hand:
;;   uv run python tools/03_emit_lisp.py --write

(eval-when (:compile-toplevel :execute :load-toplevel)
  (ql:register-local-projects)
  (ql:quickload "alexandria")
  (ql:quickload "spinneret"))

;; Repo root (this file lives there), so sbcl can run from anywhere.
(defparameter *base-dir*
  (make-pathname :name nil :type nil
		 :defaults (or *load-pathname* *default-pathname-defaults*)))

;;; BEGIN GENERATED GRAPHS
(defparameter *graph-titles*
  '(
    "Overview"
    "S-Expression Code Generators"
    "Lisp Libraries & Tools"
    "Imaging, Microscopy & Optics"
    "SDR, Radio & Radar"
    "Embedded, MCU & FPGA"
    "GPU, Graphics & Visualization"
    "Machine Learning & AI"
    "Rust Applications"
    "C/C++ Projects"
    "Web & Networking"
    "Mobile & Apps"
    "Science, Math & Simulation"
    "Finance & Trading"
    "Docs, Theses & Meta"
    ))

(defparameter *graphs*
  `(
   (;; 0 overview
     "main" "generators"
     "main" "lisp-libs"
     "main" "imaging-optics"
     "main" "sdr-radio"
     "main" "embedded-fpga"
     "main" "gpu-graphics"
     "main" "ml-ai"
     "main" "rust-apps"
     "main" "cpp-projects"
     "main" "web-net"
     "main" "mobile"
     "main" "science-math"
     "main" "finance"
     "main" "docs-meta"
    )
   (;; 1 generators (24 repos)
     "generators" "generators/ada"
     "generators" "generators/cl"
     "generators" "generators/commonlisp"
     "generators" "generators/cpp"
     "generators" "generators/cpp-generator2"
     "generators" "generators/csharp"
     "generators" "generators/elixir"
     "generators" "generators/erlang"
     "generators" "generators/golang"
     "generators" "generators/js"
     "generators" "generators/julia"
     "generators" "generators/kotlin"
     "generators" "generators/lean-py"
     "generators" "generators/matlab"
     "generators" "generators/python"
     "generators" "generators/r"
     "generators" "generators/rust"
     "generators" "generators/swift"
     "generators" "generators/tcl"
     "generators" "generators/typescript"
     "generators" "generators/vba"
     "generators" "generators/verilog"
     "generators" "generators/wolfram"
     ;; generators/ada
     "generators/ada" ("cl-ada-generator" "cl-ada-generator")
     ;; generators/cl
     "generators/cl" ("cl-cl-generator" "cl-cl-generator")
     ;; generators/commonlisp
     "generators/commonlisp" ("cl-commonlisp-generator" "cl-commonlisp-generator")
     ;; generators/cpp
     "generators/cpp" ("cl-cpp-generator" "cl-cpp-generator")
     ;; generators/cpp-generator2
     "generators/cpp-generator2" ("cl-cpp-generator2" "cl-cpp-generator2")
     ;; generators/csharp
     "generators/csharp" ("cl-csharp-generator" "cl-csharp-generator")
     ;; generators/elixir
     "generators/elixir" ("cl-elixir-generator" "cl-elixir-generator")
     ;; generators/erlang
     "generators/erlang" ("cl-erlang-generator" "cl-erlang-generator")
     ;; generators/golang
     "generators/golang" ("cl-golang-generator" "cl-golang-generator")
     ;; generators/js
     "generators/js" ("cl-js-generator" "cl-js-generator")
     ;; generators/julia
     "generators/julia" ("cl-julia-generator" "cl-julia-generator")
     ;; generators/kotlin
     "generators/kotlin" ("cl-kotlin-generator" "cl-kotlin-generator")
     ;; generators/lean-py
     "generators/lean-py" ("lean-py-generator" "lean-py-generator")
     ;; generators/matlab
     "generators/matlab" ("cl-m-generator" "cl-m-generator")
     ;; generators/python
     "generators/python" ("cl-py-generator" "cl-py-generator")
     ;; generators/r
     "generators/r" ("cl-r-generator" "cl-r-generator")
     ;; generators/rust
     "generators/rust" ("cl-rust-generator" "cl-rust-generator")
     "generators/rust" ("coalton-rust-generator" "coalton-rust-generator")
     ;; generators/swift
     "generators/swift" ("cl-swift-generator" "cl-swift-generator")
     ;; generators/tcl
     "generators/tcl" ("cl-tcl-generator" "cl-tcl-generator")
     ;; generators/typescript
     "generators/typescript" ("cl-typescript-generator" "cl-typescript-generator")
     ;; generators/vba
     "generators/vba" ("cl-vba-generator" "cl-vba-generator")
     ;; generators/verilog
     "generators/verilog" ("cl-verilog-generator" "cl-verilog-generator")
     ;; generators/wolfram
     "generators/wolfram" ("cl-wolfram-generator" "cl-wolfram-generator")
    )
   (;; 2 lisp-libs (45 repos)
     "lisp-libs" "lisp-libs/c/cl-*"
     "lisp-libs" "lisp-libs/cl-*"
     "lisp-libs" "lisp-libs/other"
     "lisp-libs" "lisp-libs/sb-*"
     ;; lisp-libs/c/cl-*
     "lisp-libs/c/cl-*" ("c-mera-ncurses" "c-mera-ncurses")
     "lisp-libs/c/cl-*" ("c-mera-ulisp" "c-mera-ulisp")
     "lisp-libs/c/cl-*" ("clicc" "clicc")
     ;; lisp-libs/cl-*
     "lisp-libs/cl-*" ("cl-bessel-zero" "cl-bessel-zero")
     "lisp-libs/cl-*" ("cl-blinkstroem" "cl-blinkstroem")
     "lisp-libs/cl-*" ("cl-cad-stl-check" "cl-cad-stl-check")
     "lisp-libs/cl-*" ("cl-cffi-callback-test" "cl-cffi-callback-test")
     "lisp-libs/cl-*" ("cl-cubic-interp" "cl-cubic-interp")
     "lisp-libs/cl-*" ("cl-data-pipes" "cl-data-pipes")
     "lisp-libs/cl-*" ("cl-gaussian-shell" "cl-gaussian-shell")
     "lisp-libs/cl-*" ("cl-learn-cells" "cl-learn-cells")
     "lisp-libs/cl-*" ("cl-linux-debug" "cl-linux-debug")
     "lisp-libs/cl-*" ("cl-pdfscan" "cl-pdfscan")
     "lisp-libs/cl-*" ("cl-pipe-run" "cl-pipe-run")
     "lisp-libs/cl-*" ("cl-pl2303" "cl-pl2303")
     "lisp-libs/cl-*" ("cl-sicp-eval" "cl-sicp-eval")
     "lisp-libs/cl-*" ("cl-try-asdf3" "cl-try-asdf3")
     "lisp-libs/cl-*" ("cl-try-cells" "cl-try-cells")
     "lisp-libs/cl-*" ("cl-try-lispworks" "cl-try-lispworks")
     "lisp-libs/cl-*" ("cl-vbox-vdi-repair" "cl-vbox-vdi-repair")
     "lisp-libs/cl-*" ("cl-vector-algebra-simplifier" "cl-vector-algebra-simplifier")
     "lisp-libs/cl-*" ("cl-week-calendar" "cl-week-calendar")
     "lisp-libs/cl-*" ("cl-yasm-golang" "cl-yasm-golang")
     ;; lisp-libs/other
     "lisp-libs/other" ("abstract-b" "abstract-b")
     "lisp-libs/other" ("ada_forth" "ada_forth")
     "lisp-libs/other" ("ada_lisp" "ada_lisp")
     "lisp-libs/other" ("array-type-dispatch" "array-type-dispatch")
     "lisp-libs/other" ("bayes" "bayes")
     "lisp-libs/other" ("ccl-headers" "ccl-headers")
     "lisp-libs/other" ("diplisp" "diplisp")
     "lisp-libs/other" ("ecl-termux-binary" "ecl-termux-binary")
     "lisp-libs/other" ("kepler" "kepler")
     "lisp-libs/other" ("kmrcl" "kmrcl")
     "lisp-libs/other" ("mycloj" "mycloj")
     "lisp-libs/other" ("nd-array-ypnos" "nd-array-ypnos")
     "lisp-libs/other" ("ogp-doc" "ogp-doc")
     "lisp-libs/other" ("ouroboros" "ouroboros")
     "lisp-libs/other" ("play_with_clasp" "play_with_clasp")
     "lisp-libs/other" ("py_try_bimpy" "py_try_bimpy")
     "lisp-libs/other" ("sicp-logic" "sicp-logic")
     "lisp-libs/other" ("try-cl-rule" "try-cl-rule")
     "lisp-libs/other" ("try_clojurescript" "try_clojurescript")
     "lisp-libs/other" ("try_ferret" "try_ferret")
     "lisp-libs/other" ("try_py2_peak_trellis" "try_py2_peak_trellis")
     ;; lisp-libs/sb-*
     "lisp-libs/sb-*" ("sb-libusb0" "sb-libusb0")
    )
   (;; 3 imaging-optics (63 repos)
     "imaging-optics" "imaging-optics/c"
     "imaging-optics" "imaging-optics/clojure"
     "imaging-optics" "imaging-optics/cpp"
     "imaging-optics" "imaging-optics/docs"
     "imaging-optics" "imaging-optics/go"
     "imaging-optics" "imaging-optics/java"
     "imaging-optics" "imaging-optics/latex"
     "imaging-optics" "imaging-optics/lisp"
     "imaging-optics" "imaging-optics/matlab"
     "imaging-optics" "imaging-optics/python"
     "imaging-optics" "imaging-optics/rust"
     "imaging-optics" "imaging-optics/unknown"
     ;; imaging-optics/c
     "imaging-optics/c" ("bacon_fb_test" "bacon_fb_test")
     "imaging-optics/c" ("interactive-cimg-c-" "interactive-cimg-c-")
     "imaging-optics/c" ("sen" "sen")
     ;; imaging-optics/clojure
     "imaging-optics/clojure" ("clj-old-code" "clj-old-code")
     ;; imaging-optics/cpp
     "imaging-optics/cpp" ("lcos-cam-calib" "lcos-cam-calib")
     "imaging-optics/cpp" ("microman-sdl-slm" "microman-sdl-slm")
     "imaging-optics/cpp" ("microman-v4l-device" "microman-v4l-device")
     "imaging-optics/cpp" ("mlib" "mlib")
     "imaging-optics/cpp" ("olcUTIL_Geometry2D" "olcUTIL_Geometry2D")
     "imaging-optics/cpp" ("opencv-eyetrack-3dwin" "opencv-eyetrack-3dwin")
     "imaging-optics/cpp" ("pnmftscale" "pnmftscale")
     "imaging-optics/cpp" ("x11_blazeface" "x11_blazeface")
     ;; imaging-optics/docs
     "imaging-optics/docs" ("basleradapter" "basleradapter")
     "imaging-optics/docs" ("zemax" "zemax")
     ;; imaging-optics/go
     "imaging-optics/go" ("quicktime_video_hack" "quicktime_video_hack")
     ;; imaging-optics/java
     "imaging-optics/java" ("View5D.jl" "View5D.jl")
     ;; imaging-optics/latex
     "imaging-optics/latex" ("camera-calib-doc" "camera-calib-doc")
     "imaging-optics/latex" ("memi-alignment" "memi-alignment")
     "imaging-optics/latex" ("mikroskopie-uebung" "mikroskopie-uebung")
     ;; imaging-optics/lisp
     "imaging-optics/lisp" ("bead-eval" "bead-eval")
     "imaging-optics/lisp" ("cl-andor" "cl-andor")
     "imaging-optics/lisp" ("cl-c2ffi-vpx" "cl-c2ffi-vpx")
     "imaging-optics/lisp" ("cl-dmd-control" "cl-dmd-control")
     "imaging-optics/lisp" ("cl-fiber-prop" "cl-fiber-prop")
     "imaging-optics/lisp" ("cl-gaussfit" "cl-gaussfit")
     "imaging-optics/lisp" ("cl-ics" "cl-ics")
     "imaging-optics/lisp" ("cl-image-processing-intro" "cl-image-processing-intro")
     "imaging-optics/lisp" ("cl-ksimpsf" "cl-ksimpsf")
     "imaging-optics/lisp" ("cl-libav" "cl-libav")
     "imaging-optics/lisp" ("cl-photon-statistics" "cl-photon-statistics")
     "imaging-optics/lisp" ("cl-v4l2" "cl-v4l2")
     "imaging-optics/lisp" ("cl-v4l2-tk" "cl-v4l2-tk")
     "imaging-optics/lisp" ("cl-vpx" "cl-vpx")
     "imaging-optics/lisp" ("cpp-hough-trafo" "cpp-hough-trafo")
     "imaging-optics/lisp" ("dic-simul" "dic-simul")
     "imaging-optics/lisp" ("fiber-holo" "fiber-holo")
     "imaging-optics/lisp" ("gauss-fit" "gauss-fit")
     "imaging-optics/lisp" ("html5_surveillance" "html5_surveillance")
     "imaging-optics/lisp" ("lcos-ogl-draw" "lcos-ogl-draw")
     "imaging-optics/lisp" ("lens" "lens")
     "imaging-optics/lisp" ("lens-doc" "lens-doc")
     "imaging-optics/lisp" ("memi-eps-pic-gen" "memi-eps-pic-gen")
     "imaging-optics/lisp" ("mma" "mma")
     "imaging-optics/lisp" ("mma-bla" "mma-bla")
     "imaging-optics/lisp" ("pifoc" "pifoc")
     "imaging-optics/lisp" ("pixel-perfect" "pixel-perfect")
     "imaging-optics/lisp" ("rescan-confocal-raytrace" "rescan-confocal-raytrace")
     "imaging-optics/lisp" ("sb-andor2-win" "sb-andor2-win")
     "imaging-optics/lisp" ("sb-fastsim" "sb-fastsim")
     "imaging-optics/lisp" ("sb-look-ma-no-libusb" "sb-look-ma-no-libusb")
     "imaging-optics/lisp" ("sb-siftfast" "sb-siftfast")
     "imaging-optics/lisp" ("sb-x264" "sb-x264")
     "imaging-optics/lisp" ("spat-bin" "spat-bin")
     "imaging-optics/lisp" ("woropt-cyb-0628" "woropt-cyb-0628")
     "imaging-optics/lisp" ("youscope" "youscope")
     ;; imaging-optics/matlab
     "imaging-optics/matlab" ("hanser-phase-retrieval" "hanser-phase-retrieval")
     "imaging-optics/matlab" ("memi" "memi")
     ;; imaging-optics/python
     "imaging-optics/python" ("afm" "afm")
     "imaging-optics/python" ("convdicom" "convdicom")
     "imaging-optics/python" ("cytometry-umap-plot" "cytometry-umap-plot")
     "imaging-optics/python" ("fcs-plotter" "fcs-plotter")
     ;; imaging-optics/rust
     "imaging-optics/rust" ("aom-decode" "aom-decode")
     ;; imaging-optics/unknown
     "imaging-optics/unknown" ("micromanager-london-kings" "micromanager-london-kings")
    )
   (;; 4 sdr-radio (10 repos)
     "sdr-radio" ("build_pluto_firmware" "build_pluto_firmware")
     "sdr-radio" ("cl-fm-radio-rds" "cl-fm-radio-rds")
     "sdr-radio" ("cl-gen-drm-waterfall" "cl-gen-drm-waterfall")
     "sdr-radio" ("cl-rust-adalm-pluto" "cl-rust-adalm-pluto")
     "sdr-radio" ("cl-rust-adalm-pluto-glfw" "cl-rust-adalm-pluto-glfw")
     "sdr-radio" ("copernicus-radar" "copernicus-radar")
     "sdr-radio" ("learn_py_iio" "learn_py_iio")
     "sdr-radio" ("linrad" "linrad")
     "sdr-radio" ("satellite-plot" "satellite-plot")
     "sdr-radio" ("satellite_hackathon" "satellite_hackathon")
    )
   (;; 5 embedded-fpga (25 repos)
     "embedded-fpga" "embedded-fpga/arduino"
     "embedded-fpga" "embedded-fpga/c"
     "embedded-fpga" "embedded-fpga/cpp"
     "embedded-fpga" "embedded-fpga/docs"
     "embedded-fpga" "embedded-fpga/js"
     "embedded-fpga" "embedded-fpga/latex"
     "embedded-fpga" "embedded-fpga/lisp"
     "embedded-fpga" "embedded-fpga/python"
     "embedded-fpga" "embedded-fpga/rust"
     "embedded-fpga" "embedded-fpga/verilog"
     "embedded-fpga" "embedded-fpga/vhdl"
     ;; embedded-fpga/arduino
     "embedded-fpga/arduino" ("Arduino_fastSIMplayingaround" "Arduino_fastSIMplayingaround")
     "embedded-fpga/arduino" ("arduino" "arduino")
     "embedded-fpga/arduino" ("arduino-stage-trigger-gen" "arduino-stage-trigger-gen")
     "embedded-fpga/arduino" ("ledtlc" "ledtlc")
     "embedded-fpga/arduino" ("picosim-arduino-due" "picosim-arduino-due")
     "embedded-fpga/arduino" ("rgb_led_matrix" "rgb_led_matrix")
     "embedded-fpga/arduino" ("ulisp-i2c" "ulisp-i2c")
     ;; embedded-fpga/c
     "embedded-fpga/c" ("etherbone-core" "etherbone-core")
     "embedded-fpga/c" ("stm32plus" "stm32plus")
     ;; embedded-fpga/cpp
     "embedded-fpga/cpp" ("esp32-c3-adc-nanopb" "esp32-c3-adc-nanopb")
     "embedded-fpga/cpp" ("pipico2w-adc-nanopb" "pipico2w-adc-nanopb")
     ;; embedded-fpga/docs
     "embedded-fpga/docs" ("JLCPCBBasicLibrary" "JLCPCBBasicLibrary")
     "embedded-fpga/docs" ("pocketbook360" "pocketbook360")
     ;; embedded-fpga/js
     "embedded-fpga/js" ("arduino-intro-talk" "arduino-intro-talk")
     ;; embedded-fpga/latex
     "embedded-fpga/latex" ("white-rabbit" "white-rabbit")
     ;; embedded-fpga/lisp
     "embedded-fpga/lisp" ("arduino_due_lisp" "arduino_due_lisp")
     "embedded-fpga/lisp" ("cl-vhdl" "cl-vhdl")
     "embedded-fpga/lisp" ("sb-linux-serial" "sb-linux-serial")
     ;; embedded-fpga/python
     "embedded-fpga/python" ("py-sam" "py-sam")
     ;; embedded-fpga/rust
     "embedded-fpga/rust" ("rp2350-cobs-proto" "rp2350-cobs-proto")
     "embedded-fpga/rust" ("wchisp" "wchisp")
     ;; embedded-fpga/verilog
     "embedded-fpga/verilog" ("K325T_SFP_PCIE_2021" "K325T_SFP_PCIE_2021")
     "embedded-fpga/verilog" ("lattice_fpga_test" "lattice_fpga_test")
     "embedded-fpga/verilog" ("led-strip" "led-strip")
     ;; embedded-fpga/vhdl
     "embedded-fpga/vhdl" ("vhdl-simulator-test" "vhdl-simulator-test")
    )
   (;; 6 gpu-graphics (45 repos)
     "gpu-graphics" "gpu-graphics/c"
     "gpu-graphics" "gpu-graphics/cpp"
     "gpu-graphics" "gpu-graphics/lisp"
     "gpu-graphics" "gpu-graphics/python"
     "gpu-graphics" "gpu-graphics/rust"
     ;; gpu-graphics/c
     "gpu-graphics/c" ("glfw" "glfw")
     "gpu-graphics/c" ("hello_quest" "hello_quest")
     "gpu-graphics/c" ("opencl-volume-raymarch" "opencl-volume-raymarch")
     "gpu-graphics/c" ("x11-shm-test" "x11-shm-test")
     ;; gpu-graphics/cpp
     "gpu-graphics/cpp" ("SuWidgets" "SuWidgets")
     "gpu-graphics/cpp" ("cl-gen-glfw" "cl-gen-glfw")
     "gpu-graphics/cpp" ("cl-gen-graphics-drm" "cl-gen-graphics-drm")
     "gpu-graphics/cpp" ("cl-gen-ispc-mandelbrot" "cl-gen-ispc-mandelbrot")
     "gpu-graphics/cpp" ("cl-gen-qt-thing" "cl-gen-qt-thing")
     "gpu-graphics/cpp" ("cl-gen2-glfw-imgui" "cl-gen2-glfw-imgui")
     "gpu-graphics/cpp" ("cl-gen2-optix" "cl-gen2-optix")
     "gpu-graphics/cpp" ("imgui" "imgui")
     "gpu-graphics/cpp" ("pge_treemap" "pge_treemap")
     "gpu-graphics/cpp" ("transpiled_treemap" "transpiled_treemap")
     "gpu-graphics/cpp" ("uVkCompute" "uVkCompute")
     "gpu-graphics/cpp" ("x11_crosshair" "x11_crosshair")
     ;; gpu-graphics/lisp
     "gpu-graphics/lisp" ("barium" "barium")
     "gpu-graphics/lisp" ("cl-3d-screen" "cl-3d-screen")
     "gpu-graphics/lisp" ("cl-c2ffi-wayland" "cl-c2ffi-wayland")
     "gpu-graphics/lisp" ("cl-cffi-gtk" "cl-cffi-gtk")
     "gpu-graphics/lisp" ("cl-cffi-gtk-from-repl" "cl-cffi-gtk-from-repl")
     "gpu-graphics/lisp" ("cl-depth-shader" "cl-depth-shader")
     "gpu-graphics/lisp" ("cl-draw-svg-bezier" "cl-draw-svg-bezier")
     "gpu-graphics/lisp" ("cl-gen-cuda-try" "cl-gen-cuda-try")
     "gpu-graphics/lisp" ("cl-gen-drmgfx" "cl-gen-drmgfx")
     "gpu-graphics/lisp" ("cl-gen-egl-compute" "cl-gen-egl-compute")
     "gpu-graphics/lisp" ("cl-gen-halide-test" "cl-gen-halide-test")
     "gpu-graphics/lisp" ("cl-gen-magnum" "cl-gen-magnum")
     "gpu-graphics/lisp" ("cl-ogl-shader" "cl-ogl-shader")
     "gpu-graphics/lisp" ("cl-online-gnuplot" "cl-online-gnuplot")
     "gpu-graphics/lisp" ("cl-pure-x11" "cl-pure-x11")
     "gpu-graphics/lisp" ("cl-raytrace-length" "cl-raytrace-length")
     "gpu-graphics/lisp" ("cl-sdl2viewer" "cl-sdl2viewer")
     "gpu-graphics/lisp" ("cl-try-iup" "cl-try-iup")
     "gpu-graphics/lisp" ("glfw-path" "glfw-path")
     "gpu-graphics/lisp" ("glraw" "glraw")
     "gpu-graphics/lisp" ("py_try_opencl" "py_try_opencl")
     "gpu-graphics/lisp" ("raspberry-pi-egl-test" "raspberry-pi-egl-test")
     "gpu-graphics/lisp" ("rayt" "rayt")
     "gpu-graphics/lisp" ("rs_disk_treemap" "rs_disk_treemap")
     "gpu-graphics/lisp" ("testglfw" "testglfw")
     ;; gpu-graphics/python
     "gpu-graphics/python" ("compare_python_plotting" "compare_python_plotting")
     "gpu-graphics/python" ("hdfogl" "hdfogl")
     "gpu-graphics/python" ("python-opengl" "python-opengl")
     ;; gpu-graphics/rust
     "gpu-graphics/rust" ("cl-rust-cuda-vis" "cl-rust-cuda-vis")
    )
   (;; 7 ml-ai (12 repos)
     "ml-ai" ("LiteRT" "LiteRT")
     "ml-ai" ("copy-cat" "copy-cat")
     "ml-ai" ("gemini-competition" "gemini-competition")
     "ml-ai" ("gemini-normalize-links" "gemini-normalize-links")
     "ml-ai" ("gemini-summary-embedding" "gemini-summary-embedding")
     "ml-ai" ("jaxopt_paper_german" "jaxopt_paper_german")
     "ml-ai" ("mnist-svd-tsne" "mnist-svd-tsne")
     "ml-ai" ("neuro-term-rs" "neuro-term-rs")
     "ml-ai" ("py_kaggle_house_price" "py_kaggle_house_price")
     "ml-ai" ("rocketrecap2" "rocketrecap2")
     "ml-ai" ("rs-summarizer" "rs-summarizer")
     "ml-ai" ("try_py_neural" "try_py_neural")
    )
   (;; 8 rust-apps (4 repos)
     "rust-apps" ("bincode" "bincode")
     "rust-apps" ("rs-example-self-update" "rs-example-self-update")
     "rust-apps" ("rust-datalib-benchmark" "rust-datalib-benchmark")
     "rust-apps" ("transcript-explorer-rs" "transcript-explorer-rs")
    )
   (;; 9 cpp-projects (10 repos)
     "cpp-projects" ("cdjb" "cdjb")
     "cpp-projects" ("cl-gen-fuzz" "cl-gen-fuzz")
     "cpp-projects" ("libcoro" "libcoro")
     "cpp-projects" ("mk-c-repl" "mk-c-repl")
     "cpp-projects" ("modern_c-" "modern_c-")
     "cpp-projects" ("pascalc" "pascalc")
     "cpp-projects" ("play_with_queues" "play_with_queues")
     "cpp-projects" ("st" "st")
     "cpp-projects" ("wld" "wld")
     "cpp-projects" ("wm" "wm")
    )
   (;; 10 web-net (19 repos)
     "web-net" "web-net/c"
     "web-net" "web-net/js"
     "web-net" "web-net/lisp"
     "web-net" "web-net/python"
     "web-net" "web-net/rust"
     "web-net" "web-net/web"
     ;; web-net/c
     "web-net/c" ("hbbp" "hbbp")
     ;; web-net/js
     "web-net/js" ("cl-aframe" "cl-aframe")
     "web-net/js" ("cl-try-matrix-js" "cl-try-matrix-js")
     "web-net/js" ("cl-try-websocket-webrtc-datachannel" "cl-try-websocket-webrtc-datachannel")
     "web-net/js" ("plops.github.io" "plops.github.io")
     ;; web-net/lisp
     "web-net/lisp" ("c_net" "c_net")
     "web-net/lisp" ("cl-gen-cpp-wasm" "cl-gen-cpp-wasm")
     "web-net/lisp" ("cl-grab-web" "cl-grab-web")
     "web-net/lisp" ("cl-web-ui" "cl-web-ui")
     "web-net/lisp" ("cl_ctl_colab" "cl_ctl_colab")
     "web-net/lisp" ("http-jq-raw-png" "http-jq-raw-png")
     "web-net/lisp" ("lisp-http" "lisp-http")
     "web-net/lisp" ("py_scrape_leb" "py_scrape_leb")
     "web-net/lisp" ("py_scrape_stuff" "py_scrape_stuff")
     "web-net/lisp" ("sb-httpd-nonblock" "sb-httpd-nonblock")
     ;; web-net/python
     "web-net/python" ("cl_ctl_linkedin" "cl_ctl_linkedin")
     "web-net/python" ("try_py_selenium" "try_py_selenium")
     ;; web-net/rust
     "web-net/rust" ("mosh-tcp" "mosh-tcp")
     ;; web-net/web
     "web-net/web" ("plops-pages" "plops-pages")
    )
   (;; 11 mobile (3 repos)
     "mobile" ("ada_sensor_fusion" "ada_sensor_fusion")
     "mobile" ("cl-gen-android-sensor" "cl-gen-android-sensor")
     "mobile" ("clj-superap" "clj-superap")
    )
   (;; 12 science-math (36 repos)
     "science-math" "science-math/cpp"
     "science-math" "science-math/latex"
     "science-math" "science-math/lisp"
     "science-math" "science-math/matlab"
     "science-math" "science-math/python"
     "science-math" "science-math/rust"
     ;; science-math/cpp
     "science-math/cpp" ("c-kdtree" "c-kdtree")
     "science-math/cpp" ("cl-gen-cufft" "cl-gen-cufft")
     "science-math/cpp" ("cl-gen-fft" "cl-gen-fft")
     "science-math/cpp" ("cpp-interp2d" "cpp-interp2d")
     "science-math/cpp" ("cpp-worm-convolve" "cpp-worm-convolve")
     "science-math/cpp" ("papipp" "papipp")
     "science-math/cpp" ("ryzen_managment_linux" "ryzen_managment_linux")
     ;; science-math/latex
     "science-math/latex" ("quartz-model" "quartz-model")
     ;; science-math/lisp
     "science-math/lisp" ("1isp-quadtree" "1isp-quadtree")
     "science-math/lisp" ("Napa-FFT3" "Napa-FFT3")
     "science-math/lisp" ("c-mera-clFFT-example" "c-mera-clFFT-example")
     "science-math/lisp" ("cl-bessel-fftw" "cl-bessel-fftw")
     "science-math/lisp" ("cl-c2ffi-nfft" "cl-c2ffi-nfft")
     "science-math/lisp" ("cl-cffi-fftw3" "cl-cffi-fftw3")
     "science-math/lisp" ("cl-fftw3" "cl-fftw3")
     "science-math/lisp" ("cl-interval-newton" "cl-interval-newton")
     "science-math/lisp" ("cl-lbfgs" "cl-lbfgs")
     "science-math/lisp" ("cl-phase-space-plot" "cl-phase-space-plot")
     "science-math/lisp" ("cl-primitive-fft" "cl-primitive-fft")
     "science-math/lisp" ("dijk" "dijk")
     "science-math/lisp" ("fem" "fem")
     "science-math/lisp" ("kdtree-90" "kdtree-90")
     "science-math/lisp" ("lisp-kdtree" "lisp-kdtree")
     "science-math/lisp" ("logic" "logic")
     "science-math/lisp" ("napa-fft3-test-2d" "napa-fft3-test-2d")
     "science-math/lisp" ("sb-hdf" "sb-hdf")
     "science-math/lisp" ("sb-nlopt" "sb-nlopt")
     "science-math/lisp" ("spiral-sample" "spiral-sample")
     ;; science-math/matlab
     "science-math/matlab" ("matlab-apotome-sim" "matlab-apotome-sim")
     "science-math/matlab" ("matlab-hilo-sim" "matlab-hilo-sim")
     "science-math/matlab" ("matlab-mma-resample-sim" "matlab-mma-resample-sim")
     "science-math/matlab" ("matlab-mma-sim" "matlab-mma-sim")
     ;; science-math/python
     "science-math/python" ("py-stars" "py-stars")
     ;; science-math/rust
     "science-math/rust" ("cl-rs-amd-uprof-viewer" "cl-rs-amd-uprof-viewer")
     "science-math/rust" ("rs-chi2-viz" "rs-chi2-viz")
     "science-math/rust" ("stars" "stars")
    )
   (;; 13 finance (2 repos)
     "finance" ("cl-py-finance" "cl-py-finance")
     "finance" ("stock-screen" "stock-screen")
    )
   (;; 14 docs-meta (28 repos)
     "docs-meta" "docs-meta/ada"
     "docs-meta" "docs-meta/docs"
     "docs-meta" "docs-meta/elisp"
     "docs-meta" "docs-meta/latex"
     "docs-meta" "docs-meta/python"
     "docs-meta" "docs-meta/rust"
     "docs-meta" "docs-meta/shell"
     "docs-meta" "docs-meta/unknown"
     "docs-meta" "docs-meta/web"
     ;; docs-meta/ada
     "docs-meta/ada" ("ada_recall_fosdem2019" "ada_recall_fosdem2019")
     "docs-meta/ada" ("learn_ada_simple_task" "learn_ada_simple_task")
     ;; docs-meta/docs
     "docs-meta/docs" ("BasicEnglishDeutschCesky" "BasicEnglishDeutschCesky")
     "docs-meta/docs" ("chinesisch-lernen" "chinesisch-lernen")
     "docs-meta/docs" ("diploma_thesis" "diploma_thesis")
     "docs-meta/docs" ("hypermedia-systems-book-summary" "hypermedia-systems-book-summary")
     "docs-meta/docs" ("mbti" "mbti")
     "docs-meta/docs" ("olisun_psych" "olisun_psych")
     "docs-meta/docs" ("phd_thesis_final" "phd_thesis_final")
     "docs-meta/docs" ("plops.github.com" "plops.github.com")
     "docs-meta/docs" ("sapkowski_in_english" "sapkowski_in_english")
     "docs-meta/docs" ("try_gh_actions" "try_gh_actions")
     "docs-meta/docs" ("virology_2025" "virology_2025")
     ;; docs-meta/elisp
     "docs-meta/elisp" ("learn_emacs_completion" "learn_emacs_completion")
     ;; docs-meta/latex
     "docs-meta/latex" ("clem-sim" "clem-sim")
     "docs-meta/latex" ("dokdok2012" "dokdok2012")
     "docs-meta/latex" ("kielhorn" "kielhorn")
     "docs-meta/latex" ("phys_chem_versuch10" "phys_chem_versuch10")
     "docs-meta/latex" ("relat" "relat")
     "docs-meta/latex" ("retreat-doc" "retreat-doc")
     "docs-meta/latex" ("thesis-review" "thesis-review")
     ;; docs-meta/python
     "docs-meta/python" ("dotemacs" "dotemacs")
     "docs-meta/python" ("github-repo-traffic-stats" "github-repo-traffic-stats")
     ;; docs-meta/rust
     "docs-meta/rust" ("slide-tag" "slide-tag")
     ;; docs-meta/shell
     "docs-meta/shell" ("pages" "pages")
     ;; docs-meta/unknown
     "docs-meta/unknown" ("right-hand-mirror-keyboard" "right-hand-mirror-keyboard")
     ;; docs-meta/web
     "docs-meta/web" ("cl_nbdev_test" "cl_nbdev_test")
     "docs-meta/web" ("nmr-seminar" "nmr-seminar")
    )
   ))
;;; END GENERATED GRAPHS

(defun svg-path (i)
  (merge-pathnames (format nil "graph~a.svg" i) *base-dir*))

(defun indexed-graphs ()
  "Triples (title svg-path) for every graph whose SVG exists."
  (loop for title in *graph-titles*
	for i from 0
	for path = (svg-path i)
	when (probe-file path)
	collect (list title path)))

(with-open-file (s (merge-pathnames "index.html" *base-dir*)
		   :direction :output
		   :if-exists :supersede
		   :if-does-not-exist :create)
  (write-sequence
   (spinneret:with-html-string
     (:doctype)
     (:html
      (:head
       (:title "plops"))
      (:body
       (:h1 "plops")
       (:p "Overview of " (:a :href "https://github.com/plops" "github.com/plops")
	   " repositories, grouped by topic. See also the "
	   (:a :href "repos_overview.md" "text overview") ".")
       (dolist (g (indexed-graphs))
	 (:h2 (first g))
	 (:raw (alexandria:read-file-into-string (second g))))
       (:h2 "presentations")
       (:ol (let ((dir (merge-pathnames "presentations/" *base-dir*)))
	      (when (probe-file dir)
		(dolist (item (directory (merge-pathnames "*.pdf" dir)))
		  (:li (:a :href (format nil "https://plops.github.io/presentations/~a.~a"
					 (pathname-name item)
					 (pathname-type item))
			       (pathname-name item))))))))))
   s))

;; pip install --user graphviz
(ql:quickload "cl-py-generator")
(in-package :cl-py-generator)

(defun get-nodes (graph)
  (let ((nodes nil))
   (loop for e in graph do
     (setf nodes (adjoin (if (listp e)
			     (first e)
			     e) nodes :test #'equal)))
    nodes))
(defun get-links (graph)
  (let ((links nil))
     (loop for e in graph do
       (when (listp e)
	 (push e links)))
    links))
(write-source (namestring (merge-pathnames "gen_graphviz"
					   cl-user::*base-dir*))
	      `(do0
		(imports (graphviz
			  os))

		,@(loop for graph in cl-user::*graphs*
			and title in cl-user::*graph-titles*
			and gi from 0
			 collect
			 (let ((nodes (get-nodes graph))
			       (links (get-links graph))
			       (g (format nil "g~a" gi)))
			   `(do0
			     (setf ,g (graphviz.Digraph :format (string "svg")
							:comment (string "projects")))
			    ,@(loop for e in nodes
				  collect
				  (let ((o (cadr (assoc e links :test #'equal))))
				    `(do0

				      ,(if o
					   `(dot ,g
						 (node
						  (string ,e)
						  :color (string "blue")
						  :URL
						  (string
						   ,(format nil
							    "https://github.com/plops/~a" o))))
					   `(dot ,g (node (string ,e)))))))
			    ,@(loop for (a b) on graph by #'cddr
				  collect
				  (let ((a1 (if (listp a)
						(first a)
						a))
					(b1 (if (listp b)
						(first b)
						b)))
				    `(dot ,g (edge (string ,a1)
						   (string ,b1)))))
			    (do0
			     (dot ,g (render))
			     (os.rename (string "Digraph.gv.svg")
					(string ,(format nil "graph~a.svg" gi)))))))
		))
