import React,{Component} from 'react';
import Dropzone from 'react-dropzone';
import request from 'superagent';

class DropZone extends Component{

  onDrop(files){
    var file = new FormData();
    file.append('name',files[0])
    var req=request
              .post('http://localhost:8000/api/v0/image/')
              .send(file);
    req.end(function(err,response){
        console.log("upload done!!!!!");
    });
  }

  render(){
    return(
      <div>
        <Dropzone onDrop={this.onDrop}>
          <div>Try dropping some files here, or click to select files to upload.</div>
        </Dropzone>
      </div>
          );
  }
}

export default DropZone;
