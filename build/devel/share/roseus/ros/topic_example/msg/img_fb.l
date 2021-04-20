;; Auto-generated. Do not edit!


(when (boundp 'topic_example::img_fb)
  (if (not (find-package "TOPIC_EXAMPLE"))
    (make-package "TOPIC_EXAMPLE"))
  (shadow 'img_fb (find-package "TOPIC_EXAMPLE")))
(unless (find-package "TOPIC_EXAMPLE::IMG_FB")
  (make-package "TOPIC_EXAMPLE::IMG_FB"))

(in-package "ROS")
;;//! \htmlinclude img_fb.msg.html


(defclass topic_example::img_fb
  :super ros::object
  :slots (_angle_fb _dist_fb ))

(defmethod topic_example::img_fb
  (:init
   (&key
    ((:angle_fb __angle_fb) 0.0)
    ((:dist_fb __dist_fb) 0.0)
    )
   (send-super :init)
   (setq _angle_fb (float __angle_fb))
   (setq _dist_fb (float __dist_fb))
   self)
  (:angle_fb
   (&optional __angle_fb)
   (if __angle_fb (setq _angle_fb __angle_fb)) _angle_fb)
  (:dist_fb
   (&optional __dist_fb)
   (if __dist_fb (setq _dist_fb __dist_fb)) _dist_fb)
  (:serialization-length
   ()
   (+
    ;; float64 _angle_fb
    8
    ;; float64 _dist_fb
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _angle_fb
       (sys::poke _angle_fb (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _dist_fb
       (sys::poke _dist_fb (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _angle_fb
     (setq _angle_fb (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _dist_fb
     (setq _dist_fb (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get topic_example::img_fb :md5sum-) "32196808a91024a033d12fa41fb8c427")
(setf (get topic_example::img_fb :datatype-) "topic_example/img_fb")
(setf (get topic_example::img_fb :definition-)
      "float64 angle_fb
float64 dist_fb
")



(provide :topic_example/img_fb "32196808a91024a033d12fa41fb8c427")


