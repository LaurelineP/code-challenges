const getActualMemorySize = value => {
    if(!(/\d{1,}[A-Z]{1}B/i.test(value))){
        throw new Error("Invalid memory size")
    }    
    const [ number = "", size = "" ] = value
        .split(/([A-Z]{2})/i, 2);

    const isSmallerThanGB = /mb/i.test(size)
    const lostPercent = number * (7 / 100);
    const result = number - lostPercent;

    const fractionDigit = isSmallerThanGB ? 0 : 2;
    result.toFixed('')
    return result.toFixed(fractionDigit) + size.toUpperCase();
}