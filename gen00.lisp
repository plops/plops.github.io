
(eval-when (:compile-toplevel :execute :load-toplevel)
  (ql:quickload "alexandria")
  (ql:quickload "spinneret"))

(with-open-file (s "index.html"
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
       (:h2 "overview")
       (:img :src "graph.svg")
       (:h2 "presentations"
	    )
       (:ol (dolist (item (directory "/home/martin/stage/plops.github.io/presentations/*.pdf"))
	      (:li (:a :href (format nil "https://plops.github.io/presentations/~a.~a" (pathname-name item)
				     (pathname-type item))
		       (pathname-name item))))))))
   s))

(defparameter *graph*
  `(
    main   sexpr
	   main   sdr
	   sdr  pluto
	   sdr  sar
	   sexpr  (cpp2 cl-cpp-generator2)
	   sexpr  (python cl-python-generator)
	   sexpr  (kotlin cl-kotlin-generator) 
	   sexpr  (rust cl-rust-generator) 
	   sexpr  (elixir cl-elixir-generator)
	   sexpr  (go cl-golang-generator)
	   sexpr  (js cl-js-generator)
	   sexpr  (matlab cl-m-generator)
	   sexpr  (swift cl-swift-generator)
	   python   finance
	   rust  cuda
	   rust  pluto
	   rust  uprof
	   cpp2  optix
	   main  android
	   cpp2  wasm
	   cpp2  cuda
	   cpp2  vulkan
	   cpp2  script
	   script lua_in_cpp
	   cpp2  tbb
	   cpp2  embed
	   embed  pluto
	   embed  psoc
	   embed  stm32
	   cpp2  sar
	   cpp2  gui
	   gui  gtk
	   gui  qt
	   gui  fltk
	   gui  imgui
	   gui  wx
	   cpp2  asio
	   cpp2  script
	   script pybind11
	   pybind11 python_in_cpp
	   cpp2  termimg
	   elixir  phx
	   python  ai
	   python  pyvulkan
	   python  autoweb
	   autoweb  helium
	   autoweb  selenium
	   python  pygui
	   pygui  pywx
	   pygui  gtk3
	   pygui  pyqt
	   pyqt webkit
	   pygui  glumpy
	   pygui  tkinter
	   pygui  visdom
	   qt  trellis
	   qt  webengine
	   python  waveguide
	   ai  megatron
	   ai  fastai
	   ai  fastai2
	   fastai2  nlp
	   ai  pytorch
	   python  numba
	   python  pycuda
	   python  cupy
	   python  dask
	   js  electron
	   kotlin  kot_opengles
	   kotlin  sensors
	   kotlin  camera
	   kotlin  renderscript
	   kotlin  grpc
	   kotlin  gps
	   kotlin  key_secure
	   kotlin  compress
	   kotlin  encrypt
	   swift  tensorflow
	   go  gogui
	   gogui fayne
	   go  gogrpc
	   go  concur_chan))

;; pip install --user graphviz
(ql:quickload "cl-py-generator")
(in-package :cl-py-generator)


(let ((nodes nil)
      (links nil))
  (loop for e in *graph* do
    (setf nodes (adjoin (if (listp e)
			    (first e)
			    e) nodes)))
  (loop for e in *graph* do
    (when (listp e)
      (push e links)))
  (defparameter *links* links)

  (write-source "/home/martin/stage/plops.github.io/gen_graphviz"
		`(do0
		  (imports (graphviz
			    os))
		  (setf g (graphviz.Digraph :format (string "svg")
					    :comment (string "projects")))
		  ,@(loop for e in nodes
			  collect
			  (let ((o (cadr (assoc e links))))
			    (if o
				`(g.node (string ,e)
					 :color (string "blue")
					 :URL
					 
					 (string ,(format nil "https://github.com/plops/~a" o)))
			     `(g.node (string ,e)
				      ))))
		  ,@(loop for (a b) on *graph* by #'cddr
			  collect
			  (let ((a1 (if (listp a)
					(first a)
					a))
				(b1 (if (listp b)
					(first b)
					b)))
			    `(g.edge (string ,a1)
				     (string ,b1))))
		  #+nil (print g.source)
		  (g.render)
		  (os.rename (string "Digraph.gv.svg")
			     (string "graph.svg")))))


