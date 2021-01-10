
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



;; pip install --user graphviz
(ql:quickload "cl-py-generator")
(in-package :cl-py-generator)
(write-source "/home/martin/stage/plops.github.io/gen_graphviz"
	      `(do0
		(imports (graphviz))
		(setf dot (Digraph :comment (string "projects")))
		))
