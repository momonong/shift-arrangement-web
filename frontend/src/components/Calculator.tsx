import { useState } from 'react';
import {calculate_get} from './Math';

const Calculator = () => {
    const [operator, setOperator] = useState<string>('add');
    const [a, setA] = useState<number>(0);
    const [b, setB] = useState<number>(0); 
    const [result, setResult] = useState<number>(0);
    const onClick = async () => {
        const result = await calculate_get(operator, a, b)
        setResult(result)
    }
    return <div>
        This is a Calculator
        <input type='number' value={a} onChange={e => setA(Number(e.target.value))}/>
        <select name="operator" id="operator" onChange={e => setOperator(e.target.value)}>
            {
                [
                    {name: 'add', text: '+'},
                    {name: 'sub', text: '-'},
                    {name: 'mul', text: '*'},
                    {name: 'div', text: '/'}
                ].map(({name, text}) => <option key={text} value={name}>{text}</option>)
            }
            {/* <option value="add">+</option>
            <option value="sub">-</option>
            <option value="mul">*</option>
            <option value="div">/</option> */}
        </select>
        <input type='number' value={b} onChange={e => setB(Number(e.target.value))}/>
        <button onClick={onClick}>Calculate {a} {operator} {b}</button>
        <div>Reslut: {result}</div>
        </div>
}

export default Calculator;