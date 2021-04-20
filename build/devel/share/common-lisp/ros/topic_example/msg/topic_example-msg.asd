
(cl:in-package :asdf)

(defsystem "topic_example-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Img_fb" :depends-on ("_package_Img_fb"))
    (:file "_package_Img_fb" :depends-on ("_package"))
  ))