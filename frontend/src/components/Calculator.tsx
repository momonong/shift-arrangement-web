import {calculate_get} from './Math'

const Calculator = () => {
    calculate_get('mul', 2, 3).then(console.log)
    return <div>hello world</div>
}

export default Calculator