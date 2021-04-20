// Auto-generated. Do not edit!

// (in-package topic_example.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Img_fb {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.angle_fb = null;
      this.dist_fb = null;
    }
    else {
      if (initObj.hasOwnProperty('angle_fb')) {
        this.angle_fb = initObj.angle_fb
      }
      else {
        this.angle_fb = 0.0;
      }
      if (initObj.hasOwnProperty('dist_fb')) {
        this.dist_fb = initObj.dist_fb
      }
      else {
        this.dist_fb = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Img_fb
    // Serialize message field [angle_fb]
    bufferOffset = _serializer.float64(obj.angle_fb, buffer, bufferOffset);
    // Serialize message field [dist_fb]
    bufferOffset = _serializer.float64(obj.dist_fb, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Img_fb
    let len;
    let data = new Img_fb(null);
    // Deserialize message field [angle_fb]
    data.angle_fb = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [dist_fb]
    data.dist_fb = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'topic_example/Img_fb';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '32196808a91024a033d12fa41fb8c427';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 angle_fb
    float64 dist_fb
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Img_fb(null);
    if (msg.angle_fb !== undefined) {
      resolved.angle_fb = msg.angle_fb;
    }
    else {
      resolved.angle_fb = 0.0
    }

    if (msg.dist_fb !== undefined) {
      resolved.dist_fb = msg.dist_fb;
    }
    else {
      resolved.dist_fb = 0.0
    }

    return resolved;
    }
};

module.exports = Img_fb;
