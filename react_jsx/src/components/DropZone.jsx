import React,{Component} from 'react';
import Dropzone from 'react-dropzone';
import request from 'superagent';

class DropZone extends Component{

  onDrop(files){
    var file = new FormData();
    // file.append('name',files[0])
    file.append('name', files[0], 'xxx.txt')
    var req=request
              .post('http://localhost:8000/api/v0/image/')
              .send(file);
    req.end(function(err,response){
      console.log(files[0].name);
      console.log(files);
      console.log("upload done!!!!!");
    });
  }

  render(){
    return(
      <div>
        <Dropzone onDrop={this.onDrop}>
          {console.log(this.onDrop)}
          <div>Try dropping some files here, or click to select files to upload.</div>
        </Dropzone>
      </div>
          );
  }
}

export default DropZone;
