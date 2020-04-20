export const listChats  = async (id) => {
    let data;
    try {	
        const chats =  await fetch(`http://127.0.0.1:8000/contact/${id}/chats`)			
        data  = chats.json();
        
    } catch (error) { 
       return error.message;
    }
    return data;
}

const validate = (number) => {
    if(number<=9){
      number ="0"+number;
    }
    return number 
}

export const systemDate = (timestamp) => {
    const fullDate = new Date(timestamp)
    const getDate = validate(fullDate.getDate());
    const getMonth = validate(fullDate.getMonth()+1);
    const getFullYear = fullDate.getFullYear()
    
    const minutes =  validate(fullDate.getMinutes());
    const seconds =  validate(fullDate.getSeconds());
    let  hours = validate(fullDate.getHours());
    
    const myClock = `${hours}:${minutes}:${seconds}`;
    const day = `${getDate}/${getMonth}/${getFullYear}`;
    const date = `${myClock} - ${day}`
    return date;  
}