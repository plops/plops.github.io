import graphviz
import os

g0 = graphviz.Digraph(format="svg", comment="projects")
g0.node("docs-meta")
g0.node("finance")
g0.node("science-math")
g0.node("mobile")
g0.node("web-net")
g0.node("cpp-projects")
g0.node("rust-apps")
g0.node("ml-ai")
g0.node("gpu-graphics")
g0.node("embedded-fpga")
g0.node("sdr-radio")
g0.node("imaging-optics")
g0.node("lisp-libs")
g0.node("generators")
g0.node("main")
g0.edge("main", "generators")
g0.edge("main", "lisp-libs")
g0.edge("main", "imaging-optics")
g0.edge("main", "sdr-radio")
g0.edge("main", "embedded-fpga")
g0.edge("main", "gpu-graphics")
g0.edge("main", "ml-ai")
g0.edge("main", "rust-apps")
g0.edge("main", "cpp-projects")
g0.edge("main", "web-net")
g0.edge("main", "mobile")
g0.edge("main", "science-math")
g0.edge("main", "finance")
g0.edge("main", "docs-meta")
g0.render()
os.rename("Digraph.gv.svg", "graph0.svg")
g1 = graphviz.Digraph(format="svg", comment="projects")
g1.node(
    "cl-wolfram-generator",
    color="blue",
    URL="https://github.com/plops/cl-wolfram-generator",
)
g1.node(
    "cl-verilog-generator",
    color="blue",
    URL="https://github.com/plops/cl-verilog-generator",
)
g1.node(
    "cl-vba-generator", color="blue", URL="https://github.com/plops/cl-vba-generator"
)
g1.node(
    "cl-typescript-generator",
    color="blue",
    URL="https://github.com/plops/cl-typescript-generator",
)
g1.node(
    "cl-tcl-generator", color="blue", URL="https://github.com/plops/cl-tcl-generator"
)
g1.node(
    "cl-swift-generator",
    color="blue",
    URL="https://github.com/plops/cl-swift-generator",
)
g1.node(
    "coalton-rust-generator",
    color="blue",
    URL="https://github.com/plops/coalton-rust-generator",
)
g1.node(
    "cl-rust-generator", color="blue", URL="https://github.com/plops/cl-rust-generator"
)
g1.node("cl-r-generator", color="blue", URL="https://github.com/plops/cl-r-generator")
g1.node("cl-py-generator", color="blue", URL="https://github.com/plops/cl-py-generator")
g1.node("cl-m-generator", color="blue", URL="https://github.com/plops/cl-m-generator")
g1.node(
    "lean-py-generator", color="blue", URL="https://github.com/plops/lean-py-generator"
)
g1.node(
    "cl-kotlin-generator",
    color="blue",
    URL="https://github.com/plops/cl-kotlin-generator",
)
g1.node(
    "cl-julia-generator",
    color="blue",
    URL="https://github.com/plops/cl-julia-generator",
)
g1.node("cl-js-generator", color="blue", URL="https://github.com/plops/cl-js-generator")
g1.node(
    "cl-golang-generator",
    color="blue",
    URL="https://github.com/plops/cl-golang-generator",
)
g1.node(
    "cl-erlang-generator",
    color="blue",
    URL="https://github.com/plops/cl-erlang-generator",
)
g1.node(
    "cl-elixir-generator",
    color="blue",
    URL="https://github.com/plops/cl-elixir-generator",
)
g1.node(
    "cl-csharp-generator",
    color="blue",
    URL="https://github.com/plops/cl-csharp-generator",
)
g1.node(
    "cl-cpp-generator2", color="blue", URL="https://github.com/plops/cl-cpp-generator2"
)
g1.node(
    "cl-cpp-generator", color="blue", URL="https://github.com/plops/cl-cpp-generator"
)
g1.node(
    "cl-commonlisp-generator",
    color="blue",
    URL="https://github.com/plops/cl-commonlisp-generator",
)
g1.node("cl-cl-generator", color="blue", URL="https://github.com/plops/cl-cl-generator")
g1.node(
    "cl-ada-generator", color="blue", URL="https://github.com/plops/cl-ada-generator"
)
g1.node("generators/wolfram")
g1.node("generators/verilog")
g1.node("generators/vba")
g1.node("generators/typescript")
g1.node("generators/tcl")
g1.node("generators/swift")
g1.node("generators/rust")
g1.node("generators/r")
g1.node("generators/python")
g1.node("generators/matlab")
g1.node("generators/lean-py")
g1.node("generators/kotlin")
g1.node("generators/julia")
g1.node("generators/js")
g1.node("generators/golang")
g1.node("generators/erlang")
g1.node("generators/elixir")
g1.node("generators/csharp")
g1.node("generators/cpp-generator2")
g1.node("generators/cpp")
g1.node("generators/commonlisp")
g1.node("generators/cl")
g1.node("generators/ada")
g1.node("generators")
g1.edge("generators", "generators/ada")
g1.edge("generators", "generators/cl")
g1.edge("generators", "generators/commonlisp")
g1.edge("generators", "generators/cpp")
g1.edge("generators", "generators/cpp-generator2")
g1.edge("generators", "generators/csharp")
g1.edge("generators", "generators/elixir")
g1.edge("generators", "generators/erlang")
g1.edge("generators", "generators/golang")
g1.edge("generators", "generators/js")
g1.edge("generators", "generators/julia")
g1.edge("generators", "generators/kotlin")
g1.edge("generators", "generators/lean-py")
g1.edge("generators", "generators/matlab")
g1.edge("generators", "generators/python")
g1.edge("generators", "generators/r")
g1.edge("generators", "generators/rust")
g1.edge("generators", "generators/swift")
g1.edge("generators", "generators/tcl")
g1.edge("generators", "generators/typescript")
g1.edge("generators", "generators/vba")
g1.edge("generators", "generators/verilog")
g1.edge("generators", "generators/wolfram")
g1.edge("generators/ada", "cl-ada-generator")
g1.edge("generators/cl", "cl-cl-generator")
g1.edge("generators/commonlisp", "cl-commonlisp-generator")
g1.edge("generators/cpp", "cl-cpp-generator")
g1.edge("generators/cpp-generator2", "cl-cpp-generator2")
g1.edge("generators/csharp", "cl-csharp-generator")
g1.edge("generators/elixir", "cl-elixir-generator")
g1.edge("generators/erlang", "cl-erlang-generator")
g1.edge("generators/golang", "cl-golang-generator")
g1.edge("generators/js", "cl-js-generator")
g1.edge("generators/julia", "cl-julia-generator")
g1.edge("generators/kotlin", "cl-kotlin-generator")
g1.edge("generators/lean-py", "lean-py-generator")
g1.edge("generators/matlab", "cl-m-generator")
g1.edge("generators/python", "cl-py-generator")
g1.edge("generators/r", "cl-r-generator")
g1.edge("generators/rust", "cl-rust-generator")
g1.edge("generators/rust", "coalton-rust-generator")
g1.edge("generators/swift", "cl-swift-generator")
g1.edge("generators/tcl", "cl-tcl-generator")
g1.edge("generators/typescript", "cl-typescript-generator")
g1.edge("generators/vba", "cl-vba-generator")
g1.edge("generators/verilog", "cl-verilog-generator")
g1.edge("generators/wolfram", "cl-wolfram-generator")
g1.render()
os.rename("Digraph.gv.svg", "graph1.svg")
g2 = graphviz.Digraph(format="svg", comment="projects")
g2.node("sb-libusb0", color="blue", URL="https://github.com/plops/sb-libusb0")
g2.node(
    "try_py2_peak_trellis",
    color="blue",
    URL="https://github.com/plops/try_py2_peak_trellis",
)
g2.node("try_ferret", color="blue", URL="https://github.com/plops/try_ferret")
g2.node(
    "try_clojurescript", color="blue", URL="https://github.com/plops/try_clojurescript"
)
g2.node("try-cl-rule", color="blue", URL="https://github.com/plops/try-cl-rule")
g2.node("sicp-logic", color="blue", URL="https://github.com/plops/sicp-logic")
g2.node("py_try_bimpy", color="blue", URL="https://github.com/plops/py_try_bimpy")
g2.node("play_with_clasp", color="blue", URL="https://github.com/plops/play_with_clasp")
g2.node("ouroboros", color="blue", URL="https://github.com/plops/ouroboros")
g2.node("ogp-doc", color="blue", URL="https://github.com/plops/ogp-doc")
g2.node("nd-array-ypnos", color="blue", URL="https://github.com/plops/nd-array-ypnos")
g2.node("mycloj", color="blue", URL="https://github.com/plops/mycloj")
g2.node("kmrcl", color="blue", URL="https://github.com/plops/kmrcl")
g2.node("kepler", color="blue", URL="https://github.com/plops/kepler")
g2.node(
    "ecl-termux-binary", color="blue", URL="https://github.com/plops/ecl-termux-binary"
)
g2.node("diplisp", color="blue", URL="https://github.com/plops/diplisp")
g2.node("ccl-headers", color="blue", URL="https://github.com/plops/ccl-headers")
g2.node("bayes", color="blue", URL="https://github.com/plops/bayes")
g2.node(
    "array-type-dispatch",
    color="blue",
    URL="https://github.com/plops/array-type-dispatch",
)
g2.node("ada_lisp", color="blue", URL="https://github.com/plops/ada_lisp")
g2.node("ada_forth", color="blue", URL="https://github.com/plops/ada_forth")
g2.node("abstract-b", color="blue", URL="https://github.com/plops/abstract-b")
g2.node("cl-yasm-golang", color="blue", URL="https://github.com/plops/cl-yasm-golang")
g2.node(
    "cl-week-calendar", color="blue", URL="https://github.com/plops/cl-week-calendar"
)
g2.node(
    "cl-vector-algebra-simplifier",
    color="blue",
    URL="https://github.com/plops/cl-vector-algebra-simplifier",
)
g2.node(
    "cl-vbox-vdi-repair",
    color="blue",
    URL="https://github.com/plops/cl-vbox-vdi-repair",
)
g2.node(
    "cl-try-lispworks", color="blue", URL="https://github.com/plops/cl-try-lispworks"
)
g2.node("cl-try-cells", color="blue", URL="https://github.com/plops/cl-try-cells")
g2.node("cl-try-asdf3", color="blue", URL="https://github.com/plops/cl-try-asdf3")
g2.node("cl-sicp-eval", color="blue", URL="https://github.com/plops/cl-sicp-eval")
g2.node("cl-pl2303", color="blue", URL="https://github.com/plops/cl-pl2303")
g2.node("cl-pipe-run", color="blue", URL="https://github.com/plops/cl-pipe-run")
g2.node("cl-pdfscan", color="blue", URL="https://github.com/plops/cl-pdfscan")
g2.node("cl-linux-debug", color="blue", URL="https://github.com/plops/cl-linux-debug")
g2.node("cl-learn-cells", color="blue", URL="https://github.com/plops/cl-learn-cells")
g2.node(
    "cl-gaussian-shell", color="blue", URL="https://github.com/plops/cl-gaussian-shell"
)
g2.node("cl-data-pipes", color="blue", URL="https://github.com/plops/cl-data-pipes")
g2.node("cl-cubic-interp", color="blue", URL="https://github.com/plops/cl-cubic-interp")
g2.node(
    "cl-cffi-callback-test",
    color="blue",
    URL="https://github.com/plops/cl-cffi-callback-test",
)
g2.node(
    "cl-cad-stl-check", color="blue", URL="https://github.com/plops/cl-cad-stl-check"
)
g2.node("cl-blinkstroem", color="blue", URL="https://github.com/plops/cl-blinkstroem")
g2.node("cl-bessel-zero", color="blue", URL="https://github.com/plops/cl-bessel-zero")
g2.node("clicc", color="blue", URL="https://github.com/plops/clicc")
g2.node("c-mera-ulisp", color="blue", URL="https://github.com/plops/c-mera-ulisp")
g2.node("c-mera-ncurses", color="blue", URL="https://github.com/plops/c-mera-ncurses")
g2.node("lisp-libs/sb-*")
g2.node("lisp-libs/other")
g2.node("lisp-libs/cl-*")
g2.node("lisp-libs/c/cl-*")
g2.node("lisp-libs")
g2.edge("lisp-libs", "lisp-libs/c/cl-*")
g2.edge("lisp-libs", "lisp-libs/cl-*")
g2.edge("lisp-libs", "lisp-libs/other")
g2.edge("lisp-libs", "lisp-libs/sb-*")
g2.edge("lisp-libs/c/cl-*", "c-mera-ncurses")
g2.edge("lisp-libs/c/cl-*", "c-mera-ulisp")
g2.edge("lisp-libs/c/cl-*", "clicc")
g2.edge("lisp-libs/cl-*", "cl-bessel-zero")
g2.edge("lisp-libs/cl-*", "cl-blinkstroem")
g2.edge("lisp-libs/cl-*", "cl-cad-stl-check")
g2.edge("lisp-libs/cl-*", "cl-cffi-callback-test")
g2.edge("lisp-libs/cl-*", "cl-cubic-interp")
g2.edge("lisp-libs/cl-*", "cl-data-pipes")
g2.edge("lisp-libs/cl-*", "cl-gaussian-shell")
g2.edge("lisp-libs/cl-*", "cl-learn-cells")
g2.edge("lisp-libs/cl-*", "cl-linux-debug")
g2.edge("lisp-libs/cl-*", "cl-pdfscan")
g2.edge("lisp-libs/cl-*", "cl-pipe-run")
g2.edge("lisp-libs/cl-*", "cl-pl2303")
g2.edge("lisp-libs/cl-*", "cl-sicp-eval")
g2.edge("lisp-libs/cl-*", "cl-try-asdf3")
g2.edge("lisp-libs/cl-*", "cl-try-cells")
g2.edge("lisp-libs/cl-*", "cl-try-lispworks")
g2.edge("lisp-libs/cl-*", "cl-vbox-vdi-repair")
g2.edge("lisp-libs/cl-*", "cl-vector-algebra-simplifier")
g2.edge("lisp-libs/cl-*", "cl-week-calendar")
g2.edge("lisp-libs/cl-*", "cl-yasm-golang")
g2.edge("lisp-libs/other", "abstract-b")
g2.edge("lisp-libs/other", "ada_forth")
g2.edge("lisp-libs/other", "ada_lisp")
g2.edge("lisp-libs/other", "array-type-dispatch")
g2.edge("lisp-libs/other", "bayes")
g2.edge("lisp-libs/other", "ccl-headers")
g2.edge("lisp-libs/other", "diplisp")
g2.edge("lisp-libs/other", "ecl-termux-binary")
g2.edge("lisp-libs/other", "kepler")
g2.edge("lisp-libs/other", "kmrcl")
g2.edge("lisp-libs/other", "mycloj")
g2.edge("lisp-libs/other", "nd-array-ypnos")
g2.edge("lisp-libs/other", "ogp-doc")
g2.edge("lisp-libs/other", "ouroboros")
g2.edge("lisp-libs/other", "play_with_clasp")
g2.edge("lisp-libs/other", "py_try_bimpy")
g2.edge("lisp-libs/other", "sicp-logic")
g2.edge("lisp-libs/other", "try-cl-rule")
g2.edge("lisp-libs/other", "try_clojurescript")
g2.edge("lisp-libs/other", "try_ferret")
g2.edge("lisp-libs/other", "try_py2_peak_trellis")
g2.edge("lisp-libs/sb-*", "sb-libusb0")
g2.render()
os.rename("Digraph.gv.svg", "graph2.svg")
g3 = graphviz.Digraph(format="svg", comment="projects")
g3.node(
    "micromanager-london-kings",
    color="blue",
    URL="https://github.com/plops/micromanager-london-kings",
)
g3.node("aom-decode", color="blue", URL="https://github.com/plops/aom-decode")
g3.node("fcs-plotter", color="blue", URL="https://github.com/plops/fcs-plotter")
g3.node(
    "cytometry-umap-plot",
    color="blue",
    URL="https://github.com/plops/cytometry-umap-plot",
)
g3.node("convdicom", color="blue", URL="https://github.com/plops/convdicom")
g3.node("afm", color="blue", URL="https://github.com/plops/afm")
g3.node("memi", color="blue", URL="https://github.com/plops/memi")
g3.node(
    "hanser-phase-retrieval",
    color="blue",
    URL="https://github.com/plops/hanser-phase-retrieval",
)
g3.node("youscope", color="blue", URL="https://github.com/plops/youscope")
g3.node("woropt-cyb-0628", color="blue", URL="https://github.com/plops/woropt-cyb-0628")
g3.node("spat-bin", color="blue", URL="https://github.com/plops/spat-bin")
g3.node("sb-x264", color="blue", URL="https://github.com/plops/sb-x264")
g3.node("sb-siftfast", color="blue", URL="https://github.com/plops/sb-siftfast")
g3.node(
    "sb-look-ma-no-libusb",
    color="blue",
    URL="https://github.com/plops/sb-look-ma-no-libusb",
)
g3.node("sb-fastsim", color="blue", URL="https://github.com/plops/sb-fastsim")
g3.node("sb-andor2-win", color="blue", URL="https://github.com/plops/sb-andor2-win")
g3.node(
    "rescan-confocal-raytrace",
    color="blue",
    URL="https://github.com/plops/rescan-confocal-raytrace",
)
g3.node("pixel-perfect", color="blue", URL="https://github.com/plops/pixel-perfect")
g3.node("pifoc", color="blue", URL="https://github.com/plops/pifoc")
g3.node("mma-bla", color="blue", URL="https://github.com/plops/mma-bla")
g3.node("mma", color="blue", URL="https://github.com/plops/mma")
g3.node(
    "memi-eps-pic-gen", color="blue", URL="https://github.com/plops/memi-eps-pic-gen"
)
g3.node("lens-doc", color="blue", URL="https://github.com/plops/lens-doc")
g3.node("lens", color="blue", URL="https://github.com/plops/lens")
g3.node("lcos-ogl-draw", color="blue", URL="https://github.com/plops/lcos-ogl-draw")
g3.node(
    "html5_surveillance",
    color="blue",
    URL="https://github.com/plops/html5_surveillance",
)
g3.node("gauss-fit", color="blue", URL="https://github.com/plops/gauss-fit")
g3.node("fiber-holo", color="blue", URL="https://github.com/plops/fiber-holo")
g3.node("dic-simul", color="blue", URL="https://github.com/plops/dic-simul")
g3.node("cpp-hough-trafo", color="blue", URL="https://github.com/plops/cpp-hough-trafo")
g3.node("cl-vpx", color="blue", URL="https://github.com/plops/cl-vpx")
g3.node("cl-v4l2-tk", color="blue", URL="https://github.com/plops/cl-v4l2-tk")
g3.node("cl-v4l2", color="blue", URL="https://github.com/plops/cl-v4l2")
g3.node(
    "cl-photon-statistics",
    color="blue",
    URL="https://github.com/plops/cl-photon-statistics",
)
g3.node("cl-libav", color="blue", URL="https://github.com/plops/cl-libav")
g3.node("cl-ksimpsf", color="blue", URL="https://github.com/plops/cl-ksimpsf")
g3.node(
    "cl-image-processing-intro",
    color="blue",
    URL="https://github.com/plops/cl-image-processing-intro",
)
g3.node("cl-ics", color="blue", URL="https://github.com/plops/cl-ics")
g3.node("cl-gaussfit", color="blue", URL="https://github.com/plops/cl-gaussfit")
g3.node("cl-fiber-prop", color="blue", URL="https://github.com/plops/cl-fiber-prop")
g3.node("cl-dmd-control", color="blue", URL="https://github.com/plops/cl-dmd-control")
g3.node("cl-c2ffi-vpx", color="blue", URL="https://github.com/plops/cl-c2ffi-vpx")
g3.node("cl-andor", color="blue", URL="https://github.com/plops/cl-andor")
g3.node("bead-eval", color="blue", URL="https://github.com/plops/bead-eval")
g3.node(
    "mikroskopie-uebung",
    color="blue",
    URL="https://github.com/plops/mikroskopie-uebung",
)
g3.node("memi-alignment", color="blue", URL="https://github.com/plops/memi-alignment")
g3.node(
    "camera-calib-doc", color="blue", URL="https://github.com/plops/camera-calib-doc"
)
g3.node("View5D.jl", color="blue", URL="https://github.com/plops/View5D.jl")
g3.node(
    "quicktime_video_hack",
    color="blue",
    URL="https://github.com/plops/quicktime_video_hack",
)
g3.node("zemax", color="blue", URL="https://github.com/plops/zemax")
g3.node("basleradapter", color="blue", URL="https://github.com/plops/basleradapter")
g3.node("x11_blazeface", color="blue", URL="https://github.com/plops/x11_blazeface")
g3.node("pnmftscale", color="blue", URL="https://github.com/plops/pnmftscale")
g3.node(
    "opencv-eyetrack-3dwin",
    color="blue",
    URL="https://github.com/plops/opencv-eyetrack-3dwin",
)
g3.node(
    "olcUTIL_Geometry2D",
    color="blue",
    URL="https://github.com/plops/olcUTIL_Geometry2D",
)
g3.node("mlib", color="blue", URL="https://github.com/plops/mlib")
g3.node(
    "microman-v4l-device",
    color="blue",
    URL="https://github.com/plops/microman-v4l-device",
)
g3.node(
    "microman-sdl-slm", color="blue", URL="https://github.com/plops/microman-sdl-slm"
)
g3.node("lcos-cam-calib", color="blue", URL="https://github.com/plops/lcos-cam-calib")
g3.node("clj-old-code", color="blue", URL="https://github.com/plops/clj-old-code")
g3.node("sen", color="blue", URL="https://github.com/plops/sen")
g3.node(
    "interactive-cimg-c-",
    color="blue",
    URL="https://github.com/plops/interactive-cimg-c-",
)
g3.node("bacon_fb_test", color="blue", URL="https://github.com/plops/bacon_fb_test")
g3.node("imaging-optics/unknown")
g3.node("imaging-optics/rust")
g3.node("imaging-optics/python")
g3.node("imaging-optics/matlab")
g3.node("imaging-optics/lisp")
g3.node("imaging-optics/latex")
g3.node("imaging-optics/java")
g3.node("imaging-optics/go")
g3.node("imaging-optics/docs")
g3.node("imaging-optics/cpp")
g3.node("imaging-optics/clojure")
g3.node("imaging-optics/c")
g3.node("imaging-optics")
g3.edge("imaging-optics", "imaging-optics/c")
g3.edge("imaging-optics", "imaging-optics/clojure")
g3.edge("imaging-optics", "imaging-optics/cpp")
g3.edge("imaging-optics", "imaging-optics/docs")
g3.edge("imaging-optics", "imaging-optics/go")
g3.edge("imaging-optics", "imaging-optics/java")
g3.edge("imaging-optics", "imaging-optics/latex")
g3.edge("imaging-optics", "imaging-optics/lisp")
g3.edge("imaging-optics", "imaging-optics/matlab")
g3.edge("imaging-optics", "imaging-optics/python")
g3.edge("imaging-optics", "imaging-optics/rust")
g3.edge("imaging-optics", "imaging-optics/unknown")
g3.edge("imaging-optics/c", "bacon_fb_test")
g3.edge("imaging-optics/c", "interactive-cimg-c-")
g3.edge("imaging-optics/c", "sen")
g3.edge("imaging-optics/clojure", "clj-old-code")
g3.edge("imaging-optics/cpp", "lcos-cam-calib")
g3.edge("imaging-optics/cpp", "microman-sdl-slm")
g3.edge("imaging-optics/cpp", "microman-v4l-device")
g3.edge("imaging-optics/cpp", "mlib")
g3.edge("imaging-optics/cpp", "olcUTIL_Geometry2D")
g3.edge("imaging-optics/cpp", "opencv-eyetrack-3dwin")
g3.edge("imaging-optics/cpp", "pnmftscale")
g3.edge("imaging-optics/cpp", "x11_blazeface")
g3.edge("imaging-optics/docs", "basleradapter")
g3.edge("imaging-optics/docs", "zemax")
g3.edge("imaging-optics/go", "quicktime_video_hack")
g3.edge("imaging-optics/java", "View5D.jl")
g3.edge("imaging-optics/latex", "camera-calib-doc")
g3.edge("imaging-optics/latex", "memi-alignment")
g3.edge("imaging-optics/latex", "mikroskopie-uebung")
g3.edge("imaging-optics/lisp", "bead-eval")
g3.edge("imaging-optics/lisp", "cl-andor")
g3.edge("imaging-optics/lisp", "cl-c2ffi-vpx")
g3.edge("imaging-optics/lisp", "cl-dmd-control")
g3.edge("imaging-optics/lisp", "cl-fiber-prop")
g3.edge("imaging-optics/lisp", "cl-gaussfit")
g3.edge("imaging-optics/lisp", "cl-ics")
g3.edge("imaging-optics/lisp", "cl-image-processing-intro")
g3.edge("imaging-optics/lisp", "cl-ksimpsf")
g3.edge("imaging-optics/lisp", "cl-libav")
g3.edge("imaging-optics/lisp", "cl-photon-statistics")
g3.edge("imaging-optics/lisp", "cl-v4l2")
g3.edge("imaging-optics/lisp", "cl-v4l2-tk")
g3.edge("imaging-optics/lisp", "cl-vpx")
g3.edge("imaging-optics/lisp", "cpp-hough-trafo")
g3.edge("imaging-optics/lisp", "dic-simul")
g3.edge("imaging-optics/lisp", "fiber-holo")
g3.edge("imaging-optics/lisp", "gauss-fit")
g3.edge("imaging-optics/lisp", "html5_surveillance")
g3.edge("imaging-optics/lisp", "lcos-ogl-draw")
g3.edge("imaging-optics/lisp", "lens")
g3.edge("imaging-optics/lisp", "lens-doc")
g3.edge("imaging-optics/lisp", "memi-eps-pic-gen")
g3.edge("imaging-optics/lisp", "mma")
g3.edge("imaging-optics/lisp", "mma-bla")
g3.edge("imaging-optics/lisp", "pifoc")
g3.edge("imaging-optics/lisp", "pixel-perfect")
g3.edge("imaging-optics/lisp", "rescan-confocal-raytrace")
g3.edge("imaging-optics/lisp", "sb-andor2-win")
g3.edge("imaging-optics/lisp", "sb-fastsim")
g3.edge("imaging-optics/lisp", "sb-look-ma-no-libusb")
g3.edge("imaging-optics/lisp", "sb-siftfast")
g3.edge("imaging-optics/lisp", "sb-x264")
g3.edge("imaging-optics/lisp", "spat-bin")
g3.edge("imaging-optics/lisp", "woropt-cyb-0628")
g3.edge("imaging-optics/lisp", "youscope")
g3.edge("imaging-optics/matlab", "hanser-phase-retrieval")
g3.edge("imaging-optics/matlab", "memi")
g3.edge("imaging-optics/python", "afm")
g3.edge("imaging-optics/python", "convdicom")
g3.edge("imaging-optics/python", "cytometry-umap-plot")
g3.edge("imaging-optics/python", "fcs-plotter")
g3.edge("imaging-optics/rust", "aom-decode")
g3.edge("imaging-optics/unknown", "micromanager-london-kings")
g3.render()
os.rename("Digraph.gv.svg", "graph3.svg")
g4 = graphviz.Digraph(format="svg", comment="projects")
g4.node(
    "satellite_hackathon",
    color="blue",
    URL="https://github.com/plops/satellite_hackathon",
)
g4.node("satellite-plot", color="blue", URL="https://github.com/plops/satellite-plot")
g4.node("linrad", color="blue", URL="https://github.com/plops/linrad")
g4.node("learn_py_iio", color="blue", URL="https://github.com/plops/learn_py_iio")
g4.node(
    "copernicus-radar", color="blue", URL="https://github.com/plops/copernicus-radar"
)
g4.node(
    "cl-rust-adalm-pluto-glfw",
    color="blue",
    URL="https://github.com/plops/cl-rust-adalm-pluto-glfw",
)
g4.node(
    "cl-rust-adalm-pluto",
    color="blue",
    URL="https://github.com/plops/cl-rust-adalm-pluto",
)
g4.node(
    "cl-gen-drm-waterfall",
    color="blue",
    URL="https://github.com/plops/cl-gen-drm-waterfall",
)
g4.node("cl-fm-radio-rds", color="blue", URL="https://github.com/plops/cl-fm-radio-rds")
g4.node(
    "build_pluto_firmware",
    color="blue",
    URL="https://github.com/plops/build_pluto_firmware",
)
g4.node("sdr-radio")
g4.edge("sdr-radio", "build_pluto_firmware")
g4.edge("sdr-radio", "cl-fm-radio-rds")
g4.edge("sdr-radio", "cl-gen-drm-waterfall")
g4.edge("sdr-radio", "cl-rust-adalm-pluto")
g4.edge("sdr-radio", "cl-rust-adalm-pluto-glfw")
g4.edge("sdr-radio", "copernicus-radar")
g4.edge("sdr-radio", "learn_py_iio")
g4.edge("sdr-radio", "linrad")
g4.edge("sdr-radio", "satellite-plot")
g4.edge("sdr-radio", "satellite_hackathon")
g4.render()
os.rename("Digraph.gv.svg", "graph4.svg")
g5 = graphviz.Digraph(format="svg", comment="projects")
g5.node(
    "vhdl-simulator-test",
    color="blue",
    URL="https://github.com/plops/vhdl-simulator-test",
)
g5.node("led-strip", color="blue", URL="https://github.com/plops/led-strip")
g5.node(
    "lattice_fpga_test", color="blue", URL="https://github.com/plops/lattice_fpga_test"
)
g5.node(
    "K325T_SFP_PCIE_2021",
    color="blue",
    URL="https://github.com/plops/K325T_SFP_PCIE_2021",
)
g5.node("wchisp", color="blue", URL="https://github.com/plops/wchisp")
g5.node(
    "rp2350-cobs-proto", color="blue", URL="https://github.com/plops/rp2350-cobs-proto"
)
g5.node("py-sam", color="blue", URL="https://github.com/plops/py-sam")
g5.node("sb-linux-serial", color="blue", URL="https://github.com/plops/sb-linux-serial")
g5.node("cl-vhdl", color="blue", URL="https://github.com/plops/cl-vhdl")
g5.node(
    "arduino_due_lisp", color="blue", URL="https://github.com/plops/arduino_due_lisp"
)
g5.node("white-rabbit", color="blue", URL="https://github.com/plops/white-rabbit")
g5.node(
    "arduino-intro-talk",
    color="blue",
    URL="https://github.com/plops/arduino-intro-talk",
)
g5.node("pocketbook360", color="blue", URL="https://github.com/plops/pocketbook360")
g5.node(
    "JLCPCBBasicLibrary",
    color="blue",
    URL="https://github.com/plops/JLCPCBBasicLibrary",
)
g5.node(
    "pipico2w-adc-nanopb",
    color="blue",
    URL="https://github.com/plops/pipico2w-adc-nanopb",
)
g5.node(
    "esp32-c3-adc-nanopb",
    color="blue",
    URL="https://github.com/plops/esp32-c3-adc-nanopb",
)
g5.node("stm32plus", color="blue", URL="https://github.com/plops/stm32plus")
g5.node("etherbone-core", color="blue", URL="https://github.com/plops/etherbone-core")
g5.node("ulisp-i2c", color="blue", URL="https://github.com/plops/ulisp-i2c")
g5.node("rgb_led_matrix", color="blue", URL="https://github.com/plops/rgb_led_matrix")
g5.node(
    "picosim-arduino-due",
    color="blue",
    URL="https://github.com/plops/picosim-arduino-due",
)
g5.node("ledtlc", color="blue", URL="https://github.com/plops/ledtlc")
g5.node(
    "arduino-stage-trigger-gen",
    color="blue",
    URL="https://github.com/plops/arduino-stage-trigger-gen",
)
g5.node("arduino", color="blue", URL="https://github.com/plops/arduino")
g5.node(
    "Arduino_fastSIMplayingaround",
    color="blue",
    URL="https://github.com/plops/Arduino_fastSIMplayingaround",
)
g5.node("embedded-fpga/vhdl")
g5.node("embedded-fpga/verilog")
g5.node("embedded-fpga/rust")
g5.node("embedded-fpga/python")
g5.node("embedded-fpga/lisp")
g5.node("embedded-fpga/latex")
g5.node("embedded-fpga/js")
g5.node("embedded-fpga/docs")
g5.node("embedded-fpga/cpp")
g5.node("embedded-fpga/c")
g5.node("embedded-fpga/arduino")
g5.node("embedded-fpga")
g5.edge("embedded-fpga", "embedded-fpga/arduino")
g5.edge("embedded-fpga", "embedded-fpga/c")
g5.edge("embedded-fpga", "embedded-fpga/cpp")
g5.edge("embedded-fpga", "embedded-fpga/docs")
g5.edge("embedded-fpga", "embedded-fpga/js")
g5.edge("embedded-fpga", "embedded-fpga/latex")
g5.edge("embedded-fpga", "embedded-fpga/lisp")
g5.edge("embedded-fpga", "embedded-fpga/python")
g5.edge("embedded-fpga", "embedded-fpga/rust")
g5.edge("embedded-fpga", "embedded-fpga/verilog")
g5.edge("embedded-fpga", "embedded-fpga/vhdl")
g5.edge("embedded-fpga/arduino", "Arduino_fastSIMplayingaround")
g5.edge("embedded-fpga/arduino", "arduino")
g5.edge("embedded-fpga/arduino", "arduino-stage-trigger-gen")
g5.edge("embedded-fpga/arduino", "ledtlc")
g5.edge("embedded-fpga/arduino", "picosim-arduino-due")
g5.edge("embedded-fpga/arduino", "rgb_led_matrix")
g5.edge("embedded-fpga/arduino", "ulisp-i2c")
g5.edge("embedded-fpga/c", "etherbone-core")
g5.edge("embedded-fpga/c", "stm32plus")
g5.edge("embedded-fpga/cpp", "esp32-c3-adc-nanopb")
g5.edge("embedded-fpga/cpp", "pipico2w-adc-nanopb")
g5.edge("embedded-fpga/docs", "JLCPCBBasicLibrary")
g5.edge("embedded-fpga/docs", "pocketbook360")
g5.edge("embedded-fpga/js", "arduino-intro-talk")
g5.edge("embedded-fpga/latex", "white-rabbit")
g5.edge("embedded-fpga/lisp", "arduino_due_lisp")
g5.edge("embedded-fpga/lisp", "cl-vhdl")
g5.edge("embedded-fpga/lisp", "sb-linux-serial")
g5.edge("embedded-fpga/python", "py-sam")
g5.edge("embedded-fpga/rust", "rp2350-cobs-proto")
g5.edge("embedded-fpga/rust", "wchisp")
g5.edge("embedded-fpga/verilog", "K325T_SFP_PCIE_2021")
g5.edge("embedded-fpga/verilog", "lattice_fpga_test")
g5.edge("embedded-fpga/verilog", "led-strip")
g5.edge("embedded-fpga/vhdl", "vhdl-simulator-test")
g5.render()
os.rename("Digraph.gv.svg", "graph5.svg")
g6 = graphviz.Digraph(format="svg", comment="projects")
g6.node(
    "cl-rust-cuda-vis", color="blue", URL="https://github.com/plops/cl-rust-cuda-vis"
)
g6.node("python-opengl", color="blue", URL="https://github.com/plops/python-opengl")
g6.node("hdfogl", color="blue", URL="https://github.com/plops/hdfogl")
g6.node(
    "compare_python_plotting",
    color="blue",
    URL="https://github.com/plops/compare_python_plotting",
)
g6.node("testglfw", color="blue", URL="https://github.com/plops/testglfw")
g6.node("rs_disk_treemap", color="blue", URL="https://github.com/plops/rs_disk_treemap")
g6.node("rayt", color="blue", URL="https://github.com/plops/rayt")
g6.node(
    "raspberry-pi-egl-test",
    color="blue",
    URL="https://github.com/plops/raspberry-pi-egl-test",
)
g6.node("py_try_opencl", color="blue", URL="https://github.com/plops/py_try_opencl")
g6.node("glraw", color="blue", URL="https://github.com/plops/glraw")
g6.node("glfw-path", color="blue", URL="https://github.com/plops/glfw-path")
g6.node("cl-try-iup", color="blue", URL="https://github.com/plops/cl-try-iup")
g6.node("cl-sdl2viewer", color="blue", URL="https://github.com/plops/cl-sdl2viewer")
g6.node(
    "cl-raytrace-length",
    color="blue",
    URL="https://github.com/plops/cl-raytrace-length",
)
g6.node("cl-pure-x11", color="blue", URL="https://github.com/plops/cl-pure-x11")
g6.node(
    "cl-online-gnuplot", color="blue", URL="https://github.com/plops/cl-online-gnuplot"
)
g6.node("cl-ogl-shader", color="blue", URL="https://github.com/plops/cl-ogl-shader")
g6.node("cl-gen-magnum", color="blue", URL="https://github.com/plops/cl-gen-magnum")
g6.node(
    "cl-gen-halide-test",
    color="blue",
    URL="https://github.com/plops/cl-gen-halide-test",
)
g6.node(
    "cl-gen-egl-compute",
    color="blue",
    URL="https://github.com/plops/cl-gen-egl-compute",
)
g6.node("cl-gen-drmgfx", color="blue", URL="https://github.com/plops/cl-gen-drmgfx")
g6.node("cl-gen-cuda-try", color="blue", URL="https://github.com/plops/cl-gen-cuda-try")
g6.node(
    "cl-draw-svg-bezier",
    color="blue",
    URL="https://github.com/plops/cl-draw-svg-bezier",
)
g6.node("cl-depth-shader", color="blue", URL="https://github.com/plops/cl-depth-shader")
g6.node(
    "cl-cffi-gtk-from-repl",
    color="blue",
    URL="https://github.com/plops/cl-cffi-gtk-from-repl",
)
g6.node("cl-cffi-gtk", color="blue", URL="https://github.com/plops/cl-cffi-gtk")
g6.node(
    "cl-c2ffi-wayland", color="blue", URL="https://github.com/plops/cl-c2ffi-wayland"
)
g6.node("cl-3d-screen", color="blue", URL="https://github.com/plops/cl-3d-screen")
g6.node("barium", color="blue", URL="https://github.com/plops/barium")
g6.node("x11_crosshair", color="blue", URL="https://github.com/plops/x11_crosshair")
g6.node("uVkCompute", color="blue", URL="https://github.com/plops/uVkCompute")
g6.node(
    "transpiled_treemap",
    color="blue",
    URL="https://github.com/plops/transpiled_treemap",
)
g6.node("pge_treemap", color="blue", URL="https://github.com/plops/pge_treemap")
g6.node("imgui", color="blue", URL="https://github.com/plops/imgui")
g6.node("cl-gen2-optix", color="blue", URL="https://github.com/plops/cl-gen2-optix")
g6.node(
    "cl-gen2-glfw-imgui",
    color="blue",
    URL="https://github.com/plops/cl-gen2-glfw-imgui",
)
g6.node("cl-gen-qt-thing", color="blue", URL="https://github.com/plops/cl-gen-qt-thing")
g6.node(
    "cl-gen-ispc-mandelbrot",
    color="blue",
    URL="https://github.com/plops/cl-gen-ispc-mandelbrot",
)
g6.node(
    "cl-gen-graphics-drm",
    color="blue",
    URL="https://github.com/plops/cl-gen-graphics-drm",
)
g6.node("cl-gen-glfw", color="blue", URL="https://github.com/plops/cl-gen-glfw")
g6.node("SuWidgets", color="blue", URL="https://github.com/plops/SuWidgets")
g6.node("x11-shm-test", color="blue", URL="https://github.com/plops/x11-shm-test")
g6.node(
    "opencl-volume-raymarch",
    color="blue",
    URL="https://github.com/plops/opencl-volume-raymarch",
)
g6.node("hello_quest", color="blue", URL="https://github.com/plops/hello_quest")
g6.node("glfw", color="blue", URL="https://github.com/plops/glfw")
g6.node("gpu-graphics/rust")
g6.node("gpu-graphics/python")
g6.node("gpu-graphics/lisp")
g6.node("gpu-graphics/cpp")
g6.node("gpu-graphics/c")
g6.node("gpu-graphics")
g6.edge("gpu-graphics", "gpu-graphics/c")
g6.edge("gpu-graphics", "gpu-graphics/cpp")
g6.edge("gpu-graphics", "gpu-graphics/lisp")
g6.edge("gpu-graphics", "gpu-graphics/python")
g6.edge("gpu-graphics", "gpu-graphics/rust")
g6.edge("gpu-graphics/c", "glfw")
g6.edge("gpu-graphics/c", "hello_quest")
g6.edge("gpu-graphics/c", "opencl-volume-raymarch")
g6.edge("gpu-graphics/c", "x11-shm-test")
g6.edge("gpu-graphics/cpp", "SuWidgets")
g6.edge("gpu-graphics/cpp", "cl-gen-glfw")
g6.edge("gpu-graphics/cpp", "cl-gen-graphics-drm")
g6.edge("gpu-graphics/cpp", "cl-gen-ispc-mandelbrot")
g6.edge("gpu-graphics/cpp", "cl-gen-qt-thing")
g6.edge("gpu-graphics/cpp", "cl-gen2-glfw-imgui")
g6.edge("gpu-graphics/cpp", "cl-gen2-optix")
g6.edge("gpu-graphics/cpp", "imgui")
g6.edge("gpu-graphics/cpp", "pge_treemap")
g6.edge("gpu-graphics/cpp", "transpiled_treemap")
g6.edge("gpu-graphics/cpp", "uVkCompute")
g6.edge("gpu-graphics/cpp", "x11_crosshair")
g6.edge("gpu-graphics/lisp", "barium")
g6.edge("gpu-graphics/lisp", "cl-3d-screen")
g6.edge("gpu-graphics/lisp", "cl-c2ffi-wayland")
g6.edge("gpu-graphics/lisp", "cl-cffi-gtk")
g6.edge("gpu-graphics/lisp", "cl-cffi-gtk-from-repl")
g6.edge("gpu-graphics/lisp", "cl-depth-shader")
g6.edge("gpu-graphics/lisp", "cl-draw-svg-bezier")
g6.edge("gpu-graphics/lisp", "cl-gen-cuda-try")
g6.edge("gpu-graphics/lisp", "cl-gen-drmgfx")
g6.edge("gpu-graphics/lisp", "cl-gen-egl-compute")
g6.edge("gpu-graphics/lisp", "cl-gen-halide-test")
g6.edge("gpu-graphics/lisp", "cl-gen-magnum")
g6.edge("gpu-graphics/lisp", "cl-ogl-shader")
g6.edge("gpu-graphics/lisp", "cl-online-gnuplot")
g6.edge("gpu-graphics/lisp", "cl-pure-x11")
g6.edge("gpu-graphics/lisp", "cl-raytrace-length")
g6.edge("gpu-graphics/lisp", "cl-sdl2viewer")
g6.edge("gpu-graphics/lisp", "cl-try-iup")
g6.edge("gpu-graphics/lisp", "glfw-path")
g6.edge("gpu-graphics/lisp", "glraw")
g6.edge("gpu-graphics/lisp", "py_try_opencl")
g6.edge("gpu-graphics/lisp", "raspberry-pi-egl-test")
g6.edge("gpu-graphics/lisp", "rayt")
g6.edge("gpu-graphics/lisp", "rs_disk_treemap")
g6.edge("gpu-graphics/lisp", "testglfw")
g6.edge("gpu-graphics/python", "compare_python_plotting")
g6.edge("gpu-graphics/python", "hdfogl")
g6.edge("gpu-graphics/python", "python-opengl")
g6.edge("gpu-graphics/rust", "cl-rust-cuda-vis")
g6.render()
os.rename("Digraph.gv.svg", "graph6.svg")
g7 = graphviz.Digraph(format="svg", comment="projects")
g7.node("try_py_neural", color="blue", URL="https://github.com/plops/try_py_neural")
g7.node("rs-summarizer", color="blue", URL="https://github.com/plops/rs-summarizer")
g7.node("rocketrecap2", color="blue", URL="https://github.com/plops/rocketrecap2")
g7.node(
    "py_kaggle_house_price",
    color="blue",
    URL="https://github.com/plops/py_kaggle_house_price",
)
g7.node("neuro-term-rs", color="blue", URL="https://github.com/plops/neuro-term-rs")
g7.node("mnist-svd-tsne", color="blue", URL="https://github.com/plops/mnist-svd-tsne")
g7.node(
    "jaxopt_paper_german",
    color="blue",
    URL="https://github.com/plops/jaxopt_paper_german",
)
g7.node(
    "gemini-summary-embedding",
    color="blue",
    URL="https://github.com/plops/gemini-summary-embedding",
)
g7.node(
    "gemini-normalize-links",
    color="blue",
    URL="https://github.com/plops/gemini-normalize-links",
)
g7.node(
    "gemini-competition",
    color="blue",
    URL="https://github.com/plops/gemini-competition",
)
g7.node("copy-cat", color="blue", URL="https://github.com/plops/copy-cat")
g7.node("LiteRT", color="blue", URL="https://github.com/plops/LiteRT")
g7.node("ml-ai")
g7.edge("ml-ai", "LiteRT")
g7.edge("ml-ai", "copy-cat")
g7.edge("ml-ai", "gemini-competition")
g7.edge("ml-ai", "gemini-normalize-links")
g7.edge("ml-ai", "gemini-summary-embedding")
g7.edge("ml-ai", "jaxopt_paper_german")
g7.edge("ml-ai", "mnist-svd-tsne")
g7.edge("ml-ai", "neuro-term-rs")
g7.edge("ml-ai", "py_kaggle_house_price")
g7.edge("ml-ai", "rocketrecap2")
g7.edge("ml-ai", "rs-summarizer")
g7.edge("ml-ai", "try_py_neural")
g7.render()
os.rename("Digraph.gv.svg", "graph7.svg")
g8 = graphviz.Digraph(format="svg", comment="projects")
g8.node(
    "transcript-explorer-rs",
    color="blue",
    URL="https://github.com/plops/transcript-explorer-rs",
)
g8.node(
    "rust-datalib-benchmark",
    color="blue",
    URL="https://github.com/plops/rust-datalib-benchmark",
)
g8.node(
    "rs-example-self-update",
    color="blue",
    URL="https://github.com/plops/rs-example-self-update",
)
g8.node("bincode", color="blue", URL="https://github.com/plops/bincode")
g8.node("rust-apps")
g8.edge("rust-apps", "bincode")
g8.edge("rust-apps", "rs-example-self-update")
g8.edge("rust-apps", "rust-datalib-benchmark")
g8.edge("rust-apps", "transcript-explorer-rs")
g8.render()
os.rename("Digraph.gv.svg", "graph8.svg")
g9 = graphviz.Digraph(format="svg", comment="projects")
g9.node("wm", color="blue", URL="https://github.com/plops/wm")
g9.node("wld", color="blue", URL="https://github.com/plops/wld")
g9.node("st", color="blue", URL="https://github.com/plops/st")
g9.node(
    "play_with_queues", color="blue", URL="https://github.com/plops/play_with_queues"
)
g9.node("pascalc", color="blue", URL="https://github.com/plops/pascalc")
g9.node("modern_c-", color="blue", URL="https://github.com/plops/modern_c-")
g9.node("mk-c-repl", color="blue", URL="https://github.com/plops/mk-c-repl")
g9.node("libcoro", color="blue", URL="https://github.com/plops/libcoro")
g9.node("cl-gen-fuzz", color="blue", URL="https://github.com/plops/cl-gen-fuzz")
g9.node("cdjb", color="blue", URL="https://github.com/plops/cdjb")
g9.node("cpp-projects")
g9.edge("cpp-projects", "cdjb")
g9.edge("cpp-projects", "cl-gen-fuzz")
g9.edge("cpp-projects", "libcoro")
g9.edge("cpp-projects", "mk-c-repl")
g9.edge("cpp-projects", "modern_c-")
g9.edge("cpp-projects", "pascalc")
g9.edge("cpp-projects", "play_with_queues")
g9.edge("cpp-projects", "st")
g9.edge("cpp-projects", "wld")
g9.edge("cpp-projects", "wm")
g9.render()
os.rename("Digraph.gv.svg", "graph9.svg")
g10 = graphviz.Digraph(format="svg", comment="projects")
g10.node("plops-pages", color="blue", URL="https://github.com/plops/plops-pages")
g10.node("mosh-tcp", color="blue", URL="https://github.com/plops/mosh-tcp")
g10.node(
    "try_py_selenium", color="blue", URL="https://github.com/plops/try_py_selenium"
)
g10.node(
    "cl_ctl_linkedin", color="blue", URL="https://github.com/plops/cl_ctl_linkedin"
)
g10.node(
    "sb-httpd-nonblock", color="blue", URL="https://github.com/plops/sb-httpd-nonblock"
)
g10.node(
    "py_scrape_stuff", color="blue", URL="https://github.com/plops/py_scrape_stuff"
)
g10.node("py_scrape_leb", color="blue", URL="https://github.com/plops/py_scrape_leb")
g10.node("lisp-http", color="blue", URL="https://github.com/plops/lisp-http")
g10.node(
    "http-jq-raw-png", color="blue", URL="https://github.com/plops/http-jq-raw-png"
)
g10.node("cl_ctl_colab", color="blue", URL="https://github.com/plops/cl_ctl_colab")
g10.node("cl-web-ui", color="blue", URL="https://github.com/plops/cl-web-ui")
g10.node("cl-grab-web", color="blue", URL="https://github.com/plops/cl-grab-web")
g10.node(
    "cl-gen-cpp-wasm", color="blue", URL="https://github.com/plops/cl-gen-cpp-wasm"
)
g10.node("c_net", color="blue", URL="https://github.com/plops/c_net")
g10.node(
    "plops.github.io", color="blue", URL="https://github.com/plops/plops.github.io"
)
g10.node(
    "cl-try-websocket-webrtc-datachannel",
    color="blue",
    URL="https://github.com/plops/cl-try-websocket-webrtc-datachannel",
)
g10.node(
    "cl-try-matrix-js", color="blue", URL="https://github.com/plops/cl-try-matrix-js"
)
g10.node("cl-aframe", color="blue", URL="https://github.com/plops/cl-aframe")
g10.node("hbbp", color="blue", URL="https://github.com/plops/hbbp")
g10.node("web-net/web")
g10.node("web-net/rust")
g10.node("web-net/python")
g10.node("web-net/lisp")
g10.node("web-net/js")
g10.node("web-net/c")
g10.node("web-net")
g10.edge("web-net", "web-net/c")
g10.edge("web-net", "web-net/js")
g10.edge("web-net", "web-net/lisp")
g10.edge("web-net", "web-net/python")
g10.edge("web-net", "web-net/rust")
g10.edge("web-net", "web-net/web")
g10.edge("web-net/c", "hbbp")
g10.edge("web-net/js", "cl-aframe")
g10.edge("web-net/js", "cl-try-matrix-js")
g10.edge("web-net/js", "cl-try-websocket-webrtc-datachannel")
g10.edge("web-net/js", "plops.github.io")
g10.edge("web-net/lisp", "c_net")
g10.edge("web-net/lisp", "cl-gen-cpp-wasm")
g10.edge("web-net/lisp", "cl-grab-web")
g10.edge("web-net/lisp", "cl-web-ui")
g10.edge("web-net/lisp", "cl_ctl_colab")
g10.edge("web-net/lisp", "http-jq-raw-png")
g10.edge("web-net/lisp", "lisp-http")
g10.edge("web-net/lisp", "py_scrape_leb")
g10.edge("web-net/lisp", "py_scrape_stuff")
g10.edge("web-net/lisp", "sb-httpd-nonblock")
g10.edge("web-net/python", "cl_ctl_linkedin")
g10.edge("web-net/python", "try_py_selenium")
g10.edge("web-net/rust", "mosh-tcp")
g10.edge("web-net/web", "plops-pages")
g10.render()
os.rename("Digraph.gv.svg", "graph10.svg")
g11 = graphviz.Digraph(format="svg", comment="projects")
g11.node("clj-superap", color="blue", URL="https://github.com/plops/clj-superap")
g11.node(
    "cl-gen-android-sensor",
    color="blue",
    URL="https://github.com/plops/cl-gen-android-sensor",
)
g11.node(
    "ada_sensor_fusion", color="blue", URL="https://github.com/plops/ada_sensor_fusion"
)
g11.node("mobile")
g11.edge("mobile", "ada_sensor_fusion")
g11.edge("mobile", "cl-gen-android-sensor")
g11.edge("mobile", "clj-superap")
g11.render()
os.rename("Digraph.gv.svg", "graph11.svg")
g12 = graphviz.Digraph(format="svg", comment="projects")
g12.node("stars", color="blue", URL="https://github.com/plops/stars")
g12.node("rs-chi2-viz", color="blue", URL="https://github.com/plops/rs-chi2-viz")
g12.node(
    "cl-rs-amd-uprof-viewer",
    color="blue",
    URL="https://github.com/plops/cl-rs-amd-uprof-viewer",
)
g12.node("py-stars", color="blue", URL="https://github.com/plops/py-stars")
g12.node("matlab-mma-sim", color="blue", URL="https://github.com/plops/matlab-mma-sim")
g12.node(
    "matlab-mma-resample-sim",
    color="blue",
    URL="https://github.com/plops/matlab-mma-resample-sim",
)
g12.node(
    "matlab-hilo-sim", color="blue", URL="https://github.com/plops/matlab-hilo-sim"
)
g12.node(
    "matlab-apotome-sim",
    color="blue",
    URL="https://github.com/plops/matlab-apotome-sim",
)
g12.node("spiral-sample", color="blue", URL="https://github.com/plops/spiral-sample")
g12.node("sb-nlopt", color="blue", URL="https://github.com/plops/sb-nlopt")
g12.node("sb-hdf", color="blue", URL="https://github.com/plops/sb-hdf")
g12.node(
    "napa-fft3-test-2d", color="blue", URL="https://github.com/plops/napa-fft3-test-2d"
)
g12.node("logic", color="blue", URL="https://github.com/plops/logic")
g12.node("lisp-kdtree", color="blue", URL="https://github.com/plops/lisp-kdtree")
g12.node("kdtree-90", color="blue", URL="https://github.com/plops/kdtree-90")
g12.node("fem", color="blue", URL="https://github.com/plops/fem")
g12.node("dijk", color="blue", URL="https://github.com/plops/dijk")
g12.node(
    "cl-primitive-fft", color="blue", URL="https://github.com/plops/cl-primitive-fft"
)
g12.node(
    "cl-phase-space-plot",
    color="blue",
    URL="https://github.com/plops/cl-phase-space-plot",
)
g12.node("cl-lbfgs", color="blue", URL="https://github.com/plops/cl-lbfgs")
g12.node(
    "cl-interval-newton",
    color="blue",
    URL="https://github.com/plops/cl-interval-newton",
)
g12.node("cl-fftw3", color="blue", URL="https://github.com/plops/cl-fftw3")
g12.node("cl-cffi-fftw3", color="blue", URL="https://github.com/plops/cl-cffi-fftw3")
g12.node("cl-c2ffi-nfft", color="blue", URL="https://github.com/plops/cl-c2ffi-nfft")
g12.node("cl-bessel-fftw", color="blue", URL="https://github.com/plops/cl-bessel-fftw")
g12.node(
    "c-mera-clFFT-example",
    color="blue",
    URL="https://github.com/plops/c-mera-clFFT-example",
)
g12.node("Napa-FFT3", color="blue", URL="https://github.com/plops/Napa-FFT3")
g12.node("1isp-quadtree", color="blue", URL="https://github.com/plops/1isp-quadtree")
g12.node("quartz-model", color="blue", URL="https://github.com/plops/quartz-model")
g12.node(
    "ryzen_managment_linux",
    color="blue",
    URL="https://github.com/plops/ryzen_managment_linux",
)
g12.node("papipp", color="blue", URL="https://github.com/plops/papipp")
g12.node(
    "cpp-worm-convolve", color="blue", URL="https://github.com/plops/cpp-worm-convolve"
)
g12.node("cpp-interp2d", color="blue", URL="https://github.com/plops/cpp-interp2d")
g12.node("cl-gen-fft", color="blue", URL="https://github.com/plops/cl-gen-fft")
g12.node("cl-gen-cufft", color="blue", URL="https://github.com/plops/cl-gen-cufft")
g12.node("c-kdtree", color="blue", URL="https://github.com/plops/c-kdtree")
g12.node("science-math/rust")
g12.node("science-math/python")
g12.node("science-math/matlab")
g12.node("science-math/lisp")
g12.node("science-math/latex")
g12.node("science-math/cpp")
g12.node("science-math")
g12.edge("science-math", "science-math/cpp")
g12.edge("science-math", "science-math/latex")
g12.edge("science-math", "science-math/lisp")
g12.edge("science-math", "science-math/matlab")
g12.edge("science-math", "science-math/python")
g12.edge("science-math", "science-math/rust")
g12.edge("science-math/cpp", "c-kdtree")
g12.edge("science-math/cpp", "cl-gen-cufft")
g12.edge("science-math/cpp", "cl-gen-fft")
g12.edge("science-math/cpp", "cpp-interp2d")
g12.edge("science-math/cpp", "cpp-worm-convolve")
g12.edge("science-math/cpp", "papipp")
g12.edge("science-math/cpp", "ryzen_managment_linux")
g12.edge("science-math/latex", "quartz-model")
g12.edge("science-math/lisp", "1isp-quadtree")
g12.edge("science-math/lisp", "Napa-FFT3")
g12.edge("science-math/lisp", "c-mera-clFFT-example")
g12.edge("science-math/lisp", "cl-bessel-fftw")
g12.edge("science-math/lisp", "cl-c2ffi-nfft")
g12.edge("science-math/lisp", "cl-cffi-fftw3")
g12.edge("science-math/lisp", "cl-fftw3")
g12.edge("science-math/lisp", "cl-interval-newton")
g12.edge("science-math/lisp", "cl-lbfgs")
g12.edge("science-math/lisp", "cl-phase-space-plot")
g12.edge("science-math/lisp", "cl-primitive-fft")
g12.edge("science-math/lisp", "dijk")
g12.edge("science-math/lisp", "fem")
g12.edge("science-math/lisp", "kdtree-90")
g12.edge("science-math/lisp", "lisp-kdtree")
g12.edge("science-math/lisp", "logic")
g12.edge("science-math/lisp", "napa-fft3-test-2d")
g12.edge("science-math/lisp", "sb-hdf")
g12.edge("science-math/lisp", "sb-nlopt")
g12.edge("science-math/lisp", "spiral-sample")
g12.edge("science-math/matlab", "matlab-apotome-sim")
g12.edge("science-math/matlab", "matlab-hilo-sim")
g12.edge("science-math/matlab", "matlab-mma-resample-sim")
g12.edge("science-math/matlab", "matlab-mma-sim")
g12.edge("science-math/python", "py-stars")
g12.edge("science-math/rust", "cl-rs-amd-uprof-viewer")
g12.edge("science-math/rust", "rs-chi2-viz")
g12.edge("science-math/rust", "stars")
g12.render()
os.rename("Digraph.gv.svg", "graph12.svg")
g13 = graphviz.Digraph(format="svg", comment="projects")
g13.node("stock-screen", color="blue", URL="https://github.com/plops/stock-screen")
g13.node("cl-py-finance", color="blue", URL="https://github.com/plops/cl-py-finance")
g13.node("finance")
g13.edge("finance", "cl-py-finance")
g13.edge("finance", "stock-screen")
g13.render()
os.rename("Digraph.gv.svg", "graph13.svg")
g14 = graphviz.Digraph(format="svg", comment="projects")
g14.node("nmr-seminar", color="blue", URL="https://github.com/plops/nmr-seminar")
g14.node("cl_nbdev_test", color="blue", URL="https://github.com/plops/cl_nbdev_test")
g14.node(
    "right-hand-mirror-keyboard",
    color="blue",
    URL="https://github.com/plops/right-hand-mirror-keyboard",
)
g14.node("pages", color="blue", URL="https://github.com/plops/pages")
g14.node("slide-tag", color="blue", URL="https://github.com/plops/slide-tag")
g14.node(
    "github-repo-traffic-stats",
    color="blue",
    URL="https://github.com/plops/github-repo-traffic-stats",
)
g14.node("dotemacs", color="blue", URL="https://github.com/plops/dotemacs")
g14.node("thesis-review", color="blue", URL="https://github.com/plops/thesis-review")
g14.node("retreat-doc", color="blue", URL="https://github.com/plops/retreat-doc")
g14.node("relat", color="blue", URL="https://github.com/plops/relat")
g14.node(
    "phys_chem_versuch10",
    color="blue",
    URL="https://github.com/plops/phys_chem_versuch10",
)
g14.node("kielhorn", color="blue", URL="https://github.com/plops/kielhorn")
g14.node("dokdok2012", color="blue", URL="https://github.com/plops/dokdok2012")
g14.node("clem-sim", color="blue", URL="https://github.com/plops/clem-sim")
g14.node(
    "learn_emacs_completion",
    color="blue",
    URL="https://github.com/plops/learn_emacs_completion",
)
g14.node("virology_2025", color="blue", URL="https://github.com/plops/virology_2025")
g14.node("try_gh_actions", color="blue", URL="https://github.com/plops/try_gh_actions")
g14.node(
    "sapkowski_in_english",
    color="blue",
    URL="https://github.com/plops/sapkowski_in_english",
)
g14.node(
    "plops.github.com", color="blue", URL="https://github.com/plops/plops.github.com"
)
g14.node(
    "phd_thesis_final", color="blue", URL="https://github.com/plops/phd_thesis_final"
)
g14.node("olisun_psych", color="blue", URL="https://github.com/plops/olisun_psych")
g14.node("mbti", color="blue", URL="https://github.com/plops/mbti")
g14.node(
    "hypermedia-systems-book-summary",
    color="blue",
    URL="https://github.com/plops/hypermedia-systems-book-summary",
)
g14.node("diploma_thesis", color="blue", URL="https://github.com/plops/diploma_thesis")
g14.node(
    "chinesisch-lernen", color="blue", URL="https://github.com/plops/chinesisch-lernen"
)
g14.node(
    "BasicEnglishDeutschCesky",
    color="blue",
    URL="https://github.com/plops/BasicEnglishDeutschCesky",
)
g14.node(
    "learn_ada_simple_task",
    color="blue",
    URL="https://github.com/plops/learn_ada_simple_task",
)
g14.node(
    "ada_recall_fosdem2019",
    color="blue",
    URL="https://github.com/plops/ada_recall_fosdem2019",
)
g14.node("docs-meta/web")
g14.node("docs-meta/unknown")
g14.node("docs-meta/shell")
g14.node("docs-meta/rust")
g14.node("docs-meta/python")
g14.node("docs-meta/latex")
g14.node("docs-meta/elisp")
g14.node("docs-meta/docs")
g14.node("docs-meta/ada")
g14.node("docs-meta")
g14.edge("docs-meta", "docs-meta/ada")
g14.edge("docs-meta", "docs-meta/docs")
g14.edge("docs-meta", "docs-meta/elisp")
g14.edge("docs-meta", "docs-meta/latex")
g14.edge("docs-meta", "docs-meta/python")
g14.edge("docs-meta", "docs-meta/rust")
g14.edge("docs-meta", "docs-meta/shell")
g14.edge("docs-meta", "docs-meta/unknown")
g14.edge("docs-meta", "docs-meta/web")
g14.edge("docs-meta/ada", "ada_recall_fosdem2019")
g14.edge("docs-meta/ada", "learn_ada_simple_task")
g14.edge("docs-meta/docs", "BasicEnglishDeutschCesky")
g14.edge("docs-meta/docs", "chinesisch-lernen")
g14.edge("docs-meta/docs", "diploma_thesis")
g14.edge("docs-meta/docs", "hypermedia-systems-book-summary")
g14.edge("docs-meta/docs", "mbti")
g14.edge("docs-meta/docs", "olisun_psych")
g14.edge("docs-meta/docs", "phd_thesis_final")
g14.edge("docs-meta/docs", "plops.github.com")
g14.edge("docs-meta/docs", "sapkowski_in_english")
g14.edge("docs-meta/docs", "try_gh_actions")
g14.edge("docs-meta/docs", "virology_2025")
g14.edge("docs-meta/elisp", "learn_emacs_completion")
g14.edge("docs-meta/latex", "clem-sim")
g14.edge("docs-meta/latex", "dokdok2012")
g14.edge("docs-meta/latex", "kielhorn")
g14.edge("docs-meta/latex", "phys_chem_versuch10")
g14.edge("docs-meta/latex", "relat")
g14.edge("docs-meta/latex", "retreat-doc")
g14.edge("docs-meta/latex", "thesis-review")
g14.edge("docs-meta/python", "dotemacs")
g14.edge("docs-meta/python", "github-repo-traffic-stats")
g14.edge("docs-meta/rust", "slide-tag")
g14.edge("docs-meta/shell", "pages")
g14.edge("docs-meta/unknown", "right-hand-mirror-keyboard")
g14.edge("docs-meta/web", "cl_nbdev_test")
g14.edge("docs-meta/web", "nmr-seminar")
g14.render()
os.rename("Digraph.gv.svg", "graph14.svg")
