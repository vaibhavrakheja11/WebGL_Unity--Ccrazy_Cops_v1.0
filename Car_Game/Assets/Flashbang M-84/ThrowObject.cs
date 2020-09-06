using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ThrowObject : MonoBehaviour
{
    // Start is called before the first frame update
    
    public GameObject Flashbang;

    GameObject Flash;

    public float force = 10;


    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if(Input.GetMouseButtonUp(0))
        {
            Flash = Instantiate(Flashbang, transform.position + transform.forward, Quaternion.identity) as GameObject;
        Flash.AddComponent<Rigidbody>();
        Flash.GetComponent<Rigidbody>().AddForce(transform.forward * force, ForceMode.Impulse);
        Flash.AddComponent<Flashbang>();
        Flash.GetComponent<Flashbang>().player = transform;

        }
        
        
        

    }
}
