const getExtension = (fileName) =>{
   return fileName.split('.').pop();
}

getExtension("hello.pdf"); //pdf
