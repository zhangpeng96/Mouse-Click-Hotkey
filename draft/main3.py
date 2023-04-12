from pynput.keyboard import Key,Controller,Listener
 
record_key = []
 
def on_press(key):                
    record_key.append(str(key))
    
def on_release(key): 
    print(record_key)
    if 'Key.cmd' in record_key:
        if "'z'" in record_key:
            Web_search()
        if 'Key.alt_l' in record_key:
            DB_search()
    if len(record_key)>0:
        record_key.remove(str(key))
    if key == Key.esc: 
        return False
        
def Web_search():
    print('enter Web_search!')
    
def DB_search():
    print('enter DB_search!')
    
if __name__ == '__main__':
    with Listener( 
        on_press = on_press,
        on_release = on_release) as listener:
        listener.join()

