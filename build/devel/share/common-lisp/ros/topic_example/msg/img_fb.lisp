; Auto-generated. Do not edit!


(cl:in-package topic_example-msg)


;//! \htmlinclude img_fb.msg.html

(cl:defclass <img_fb> (roslisp-msg-protocol:ros-message)
  ((angle_fb
    :reader angle_fb
    :initarg :angle_fb
    :type cl:float
    :initform 0.0)
   (dist_fb
    :reader dist_fb
    :initarg :dist_fb
    :type cl:float
    :initform 0.0))
)

(cl:defclass img_fb (<img_fb>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <img_fb>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'img_fb)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name topic_example-msg:<img_fb> is deprecated: use topic_example-msg:img_fb instead.")))

(cl:ensure-generic-function 'angle_fb-val :lambda-list '(m))
(cl:defmethod angle_fb-val ((m <img_fb>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader topic_example-msg:angle_fb-val is deprecated.  Use topic_example-msg:angle_fb instead.")
  (angle_fb m))

(cl:ensure-generic-function 'dist_fb-val :lambda-list '(m))
(cl:defmethod dist_fb-val ((m <img_fb>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader topic_example-msg:dist_fb-val is deprecated.  Use topic_example-msg:dist_fb instead.")
  (dist_fb m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <img_fb>) ostream)
  "Serializes a message object of type '<img_fb>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'angle_fb))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'dist_fb))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <img_fb>) istream)
  "Deserializes a message object of type '<img_fb>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle_fb) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'dist_fb) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<img_fb>)))
  "Returns string type for a message object of type '<img_fb>"
  "topic_example/img_fb")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'img_fb)))
  "Returns string type for a message object of type 'img_fb"
  "topic_example/img_fb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<img_fb>)))
  "Returns md5sum for a message object of type '<img_fb>"
  "32196808a91024a033d12fa41fb8c427")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'img_fb)))
  "Returns md5sum for a message object of type 'img_fb"
  "32196808a91024a033d12fa41fb8c427")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<img_fb>)))
  "Returns full string definition for message of type '<img_fb>"
  (cl:format cl:nil "float64 angle_fb~%float64 dist_fb~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'img_fb)))
  "Returns full string definition for message of type 'img_fb"
  (cl:format cl:nil "float64 angle_fb~%float64 dist_fb~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <img_fb>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <img_fb>))
  "Converts a ROS message object to a list"
  (cl:list 'img_fb
    (cl:cons ':angle_fb (angle_fb msg))
    (cl:cons ':dist_fb (dist_fb msg))
))
