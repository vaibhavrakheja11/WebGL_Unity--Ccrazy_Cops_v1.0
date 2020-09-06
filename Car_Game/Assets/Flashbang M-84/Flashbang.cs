using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Flashbang : MonoBehaviour
{
    // Start is called before the first frame update

    public float MaxTimer = 7;
    float timer;

     public Transform player;

     bool cap;
     CaptureScreen captureScreen;
     bool once;




    void Start()
    {
        captureScreen = Camera.main.transform.GetComponent<CaptureScreen>();
        
    }

    // Update is called once per frame
    void Update()
    {
        timer += Time.deltaTime;

        if(timer > MaxTimer)
        {
            if(!once)
            {
                if(Vector3.Angle(player.transform.forward, transform.position - player.transform.position) < 110)
                {
                    captureScreen.startFading = true;
                    captureScreen.cap = true;
                }
                once = true;
            }
            if(timer>MaxTimer+1)
            {
                Destroy(gameObject);
            }
        }
        
    }
}
